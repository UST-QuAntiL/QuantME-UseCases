import threading
import codecs
import pickle
import base64
import json
import os
import numpy as np
from qiskit import *
from urllib.request import urlopen
import requests


def send_error(errorCode, externalTaskId):
    body = {
        "workerId": "QSVMOptimizerService",
        "errorCode": errorCode
    }
    response = requests.post(pollingEndpoint + '/' + externalTaskId + '/bpmnError', json=body)
    print(response.status_code)


def poll():
    print('Polling for new external tasks at the Camunda engine with URL: ', pollingEndpoint)

    body = {
        "workerId": "QSVMOptimizerService",
        "maxTasks": 1,
        "topics":
            [{"topicName": topic,
              "lockDuration": 100000000
              }]
    }

    try:
        response = requests.post(pollingEndpoint + '/fetchAndLock', json=body)

        if response.status_code == 200:
            for externalTask in response.json():
                print('External task with ID for topic ' + str(externalTask.get('topicName')) + ': ' + str(
                    externalTask.get('id')))
                variables = externalTask.get('variables')
                if externalTask.get('topicName') == topic:
                    if ('cluster_mapping' in variables) & ('qsvm_results' in variables) & ('thetas' in variables) \
                            & ('iterations' in variables) & ('delta' in variables) & ('data' in variables) & (
                            'circuit_template' in variables):
                        if variables.get("data").get("type") == "String":
                            data = variables.get("data").get("value")
                        else:
                            data = download_data(camundaEndpoint + "/process-instance/" + externalTask.get("processInstanceId") + "/variables/data/data")
                        if variables.get("cluster_mapping").get("type") == "String":
                            cluster_mapping = variables.get("cluster_mapping").get("value")
                        else:
                            cluster_mapping = download_data(camundaEndpoint + "/process-instance/" + externalTask.get("processInstanceId") + "/variables/cluster_mapping/data")
                        if variables.get("thetas").get("type") == "String":
                            thetas = variables.get("thetas").get("value")
                        else:
                            thetas = download_data(camundaEndpoint + "/process-instance/" + externalTask.get("processInstanceId") + "/variables/thetas/data")
                        if variables.get("iterations").get("type") == "String":
                            iterations = variables.get("iterations").get("value")
                        else:
                            iterations = download_data(camundaEndpoint + "/process-instance/" + externalTask.get("processInstanceId") + "/variables/iterations/data")
                        if variables.get("delta").get("type") == "String":
                            delta = variables.get("delta").get("value")
                        else:
                            delta = download_data(camundaEndpoint + "/process-instance/" + externalTask.get("processInstanceId") + "/variables/delta/data")
                        if variables.get("qsvm_results").get("type") == "String":
                            qsvm_results = variables.get("qsvm_results").get("value")
                        else:
                            qsvm_results = download_data(camundaEndpoint + "/process-instance/" + externalTask.get("processInstanceId") + "/variables/qsvm_results/data")
                        if variables.get("circuit_template").get("type") == "String":
                            circuit_template = variables.get("circuit_template").get("value")
                        else:
                            circuit_template = download_data(camundaEndpoint + "/process-instance/" + externalTask.get("processInstanceId") + "/variables/circuit_template/data")

                        parameterizations, thetas, thetas_plus, thetas_minus, delta, iterations, classificationConverged = execute(
                            data,
                            cluster_mapping,
                            thetas,
                            iterations,
                            qsvm_results,
                            delta,
                            circuit_template)

                        # encode parameterizations as file due to the string size limitation of camunda
                        encoded_parameterizations = base64.b64encode(str.encode(parameterizations)).decode("utf-8")

                        # send response
                        body = {
                            "workerId": "QSVMOptimizerService",
                            "variables":
                                {"thetas": {"value": thetas, "type": "String"},
                                 "thetas_plus": {"value": thetas_plus, "type": "String"},
                                 "thetas_minus": {"value": thetas_minus, "type": "String"},
                                 "delta": {"value": delta, "type": "String"},
                                 "classificationConverged": {"value": classificationConverged, "type": "String"},
                                 "iterations": {"value": iterations, "type": "String"},
                                 "parameterizations": {"value": encoded_parameterizations,
                                                       "type": "File",
                                                       "valueInfo": {
                                                           "filename": "parameterizations.txt",
                                                           "encoding": ""
                                                       }
                                                       }
                                 }
                        }
                        response = requests.post(pollingEndpoint + '/' + externalTask.get('id') + '/complete',
                                                 json=body)
                        print('Status code of response message: ' + str(response.status_code))
                    else:
                        send_error("Executing QSVM failed", externalTask.get('id'))
    except:
        print('Exception during polling!')

    threading.Timer(3, poll).start()


def download_data(url):
    response = urlopen(url)
    data = response.read().decode('utf-8')
    return str(data)


def text_to_array(text):
    text_lines = list(filter(None, text.split("\n")))
    data_array = np.zeros(shape=(len(text_lines), 2))
    for idx, data_line in enumerate(text_lines):
        for idy, val2 in enumerate(data_line.split(" ")):
            data_array[idx][idy] = float(val2)
    return data_array


def compute_probabilities(results, n_classes):
    predicted_probs = []
    predicted_labels = []
    probs = return_probabilities(results, n_classes)
    predicted_probs.append(probs)
    predicted_labels.append(np.argmax(probs, axis=1))

    if len(predicted_probs) == 1:
        predicted_probs = predicted_probs[0]
    if len(predicted_labels) == 1:
        predicted_labels = predicted_labels[0]

    return predicted_probs, predicted_labels


def get_c_spsa(iteration, optimizer_params):
    c0, c1, c2, c3, c4 = optimizer_params
    return float(c1) / np.power(iteration + 1, c3)


def get_a_spsa(iteration, optimizer_params):
    c0, c1, c2, c3, c4 = optimizer_params
    return float(c0) / np.power(iteration + 1 + c4, c2)


def gen_delta(size):
    return 2 * np.random.default_rng().integers(2, size=size) - 1


def generate_directions(iteration, thetas, optimizer_params):
    c_spsa = get_c_spsa(iteration, optimizer_params)
    delta = gen_delta(size=thetas.shape[0])

    thetas_plus = thetas + c_spsa * delta
    thetas_minus = thetas - c_spsa * delta
    return thetas_plus, thetas_minus, delta


def generate_circuit_parameterizations(circuit, data: list, thetas: list):
    fm_parameters, var_parameters = circuit[0][0].params, circuit[1][0].params
    fm_parameters, var_parameters = [param.name for param in fm_parameters], [param.name for param in var_parameters]

    parameterizations = []
    for theta in thetas:
        for datum in data:
            curr_params = dict(zip(fm_parameters, datum))
            curr_params.update(dict(zip(var_parameters, theta)))
            parameterizations.append(curr_params)

    return parameterizations


def assign_label(measured_key, num_classes):
    measured_key = np.asarray([int(k) for k in list(measured_key)])
    num_qubits = len(measured_key)
    if num_classes == 2:
        if num_qubits % 2 != 0:
            total = np.sum(measured_key)
            return 1 if total > num_qubits / 2 else 0
        else:
            hamming_weight = np.sum(measured_key)
            is_odd_parity = hamming_weight % 2
            return is_odd_parity

    elif num_classes == 3:
        first_half = int(np.floor(num_qubits / 2))
        modulo = num_qubits % 2
        # First half of key
        hamming_weight_1 = np.sum(measured_key[0:first_half + modulo])
        # Second half of key
        hamming_weight_2 = np.sum(measured_key[first_half + modulo:])
        is_odd_parity_1 = hamming_weight_1 % 2
        is_odd_parity_2 = hamming_weight_2 % 2

        return is_odd_parity_1 + is_odd_parity_2

    else:
        total_size = 2**num_qubits
        class_step = np.floor(total_size / num_classes)

        decimal_value = measured_key.dot(1 << np.arange(measured_key.shape[-1] - 1, -1, -1))
        key_order = int(decimal_value / class_step)
        return key_order if key_order < num_classes else num_classes - 1


def return_probabilities(counts, num_classes):
    probs = np.zeros(((len(counts), num_classes)))
    for idx in range(len(counts)):
        count = counts[idx]
        shots = sum(count.values())
        for k, v in count.items():
            label = assign_label(k, num_classes)
            probs[idx][label] += v / shots
    return probs


def cross_entropy(predictions, targets, epsilon=1e-12):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    tmp = np.sum(targets*np.log(predictions), axis=1)
    ce = -np.sum(tmp)/N
    return ce


def cost_estimate(probs, gt_labels, shots=None):
    mylabels = np.zeros(probs.shape)
    for i in range(gt_labels.shape[0]):
        whichindex = gt_labels[i]
        mylabels[i][whichindex] = 1

    x = cross_entropy(probs, mylabels)
    return x


def optimize(results, labels, thetas, delta, iteration, optimizer_params):
    # separate results for theta, theta_plus, and theta_minus
    results_curr, results_plus, results_minus = np.array_split(results, 3)

    # calculate probabilities
    probs_plus, pred_lbls_plus = compute_probabilities(results_plus, len(set(labels)))
    probs_minus, pred_lbls_minus = compute_probabilities(results_minus, len(set(labels)))
    probs_curr, pred_lbls_curr = compute_probabilities(results_curr, len(set(labels)))

    # calculate costs
    costs_plus = cost_estimate(probs_plus, labels)
    costs_minus = cost_estimate(probs_minus, labels)
    costs_curr = cost_estimate(probs_curr, labels)

    # updated theta
    c_spsa = get_c_spsa(iteration, optimizer_params)
    g_spsa = (costs_plus - costs_minus) * delta / (2.0 * c_spsa)
    a_spsa = get_a_spsa(iteration, optimizer_params)
    thetas = thetas - a_spsa * g_spsa
    thetas_plus, thetas_minus, delta = generate_directions(iteration, thetas, optimizer_params)

    return thetas, thetas_plus, thetas_minus, delta, costs_curr


def execute(data, cluster_mapping, thetas, iterations, qsvm_results, delta, circuit_template):
    print('Optimizing QSVM...')

    # load required data
    iterations = int(iterations)
    data_array = text_to_array(data)
    qsvm_results_list = np.array(json.loads(qsvm_results))
    thetas_list = np.array(json.loads(thetas))
    delta_list = np.array(json.loads(delta))
    cluster_mapping_list = np.array(json.loads(cluster_mapping))
    optimizer_parameters = [0.6283185307179586, 0.1, 0.602, 0.101, 0]

    # make that sure labels are integers
    cluster_mapping_list = cluster_mapping_list.astype(int)

    # perform optimization
    thetas, thetas_plus, thetas_minus, delta, costs_curr = optimize(qsvm_results_list, cluster_mapping_list,
                                                                    thetas_list, delta_list, iterations,
                                                                    optimizer_parameters)

    # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
    circuit_template = pickle.loads(codecs.decode(circuit_template.encode(), "base64"))

    # generate parametrization
    thetas_array = []
    for t in [thetas, thetas_plus, thetas_minus]:
        if t is not None:
            thetas_array.append(t)
    parameterizations = generate_circuit_parameterizations(circuit_template, data_array, thetas_array)
    print('Number of parameterizations: ', len(parameterizations))

    # check convergence
    iterations = iterations + 1
    classificationConverged = (costs_curr < 0.2) | (iterations > 30)
    classificationConverged = str(classificationConverged).lower()
    print('Converged:', classificationConverged)

    return str(json.dumps(parameterizations)), str(json.dumps(thetas.tolist())), str(json.dumps(thetas_plus.tolist())), \
        str(json.dumps(thetas_minus.tolist())), str(json.dumps(delta.tolist())), str(iterations), \
        str(classificationConverged)


camundaEndpoint = os.environ['CAMUNDA_ENDPOINT']
pollingEndpoint = camundaEndpoint + '/external-task'
#topic = os.environ['CAMUNDA_TOPIC']

topic = os.environ['CAMUNDA_TOPIC']
poll()
