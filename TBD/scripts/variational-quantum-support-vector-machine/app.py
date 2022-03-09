import asyncio
import aiohttp
import pickle
import tempfile
import math
import numpy as np
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit.providers.aer import Aer
from qiskit.providers.ibmq import IBMQ
from qiskit.circuit.library import ZFeatureMap, TwoLocal
from qiskit.utils import QuantumInstance

default_optimizer_params = [0.6283185307179586, 0.1, 0.602, 0.101, 0]


def optimize_results(results, labels, thetas, delta, iteration, optimizer_params, is_statevector=False):
    """
        Parameters:
        - results: list of results to evaluate
            (results for theta, theta_plus, theta_minus in 3 equal portions and this exact order)
            OR (results for theta_plus, theta_minus in 2 equal portions in this exact order, see exact_costs parameter)
            The results are of type qiskit.result.Result
        - labels: array, the actual labels of the data (in correct order of course)
        - thetas: array, thetas used to generate these results (i.e. thetas of the current iteration
        - delta: array, analogous to thetas
        - iteration: int, current iteration
        - optimizer_params: array, parameters c0 through c4 for optimization (floats)
        - is_statevector: bool, states whether the results were computed on a statevector simulator or not
        - exact_costs: bool, this refers to the format of results. If True then results will
            be split into three portions, else into two (for theta_plus/theta_minus only)

        Returns: thetas, thetas_plus, thetas_minus, delta for next iteration (as arrays);
            costs_curr: float, the current costs. If compute_current_cost is True it will give
            the exact current costs, otherwise those for theta_minus which are close to the current costs
    """

    n_results = len(results.results)
    n_data = len(labels)
    n_classes = len(set(labels))
    exact_costs = n_results // n_data == 3  # determines whether results contain data for thetas/exact costs computation

    results_curr = results if exact_costs else None
    results_plus, results_minus = results, results
    indices_curr, indices_plus, indices_minus = None, None, None
    if (exact_costs):
        indices_curr, indices_plus, indices_minus = np.array_split(range(3 * n_data), 3)
    else:
        indices_plus, indices_minus = np.array_split(range(2 * n_data), 2)

    probs_plus, pred_lbls_plus = computeProbabilities(results_plus, is_statevector, n_data, n_classes,
                                                      indices=indices_plus)
    probs_minus, pred_lbls_minus = computeProbabilities(results_minus, is_statevector, n_data, n_classes,
                                                        indices=indices_minus)
    costs_plus = cost_estimate(probs_plus, labels)
    costs_minus = cost_estimate(probs_minus, labels)

    costs_curr = None
    if (results_curr is not None):
        probs_curr, pred_lbls_curr = computeProbabilities(results_curr, is_statevector, n_data, n_classes,
                                                          indices=indices_curr)
        costs_curr = cost_estimate(probs_curr, labels)
    else:
        costs_curr = costs_minus

    g_spsa = (costs_plus - costs_minus) * delta / (2.0 * get_c_spsa(iteration, optimizer_params))

    # updated theta
    thetas = thetas - get_a_spsa(iteration, optimizer_params) * g_spsa

    thetas_plus, thetas_minus, delta = generateDirections(iteration, thetas, optimizer_params)

    return thetas, thetas_plus, thetas_minus, delta, costs_curr


def gen_delta(size):
    return 2 * np.random.default_rng().integers(2, size=size) - 1


def generateDirections(iteration, thetas, optimizer_params):
    c_spsa = get_c_spsa(iteration, optimizer_params)
    delta = gen_delta(size=thetas.shape[0])

    thetas_plus = thetas + c_spsa * delta
    thetas_minus = thetas - c_spsa * delta
    return thetas_plus, thetas_minus, delta


def get_a_spsa(iteration, optimizer_params):
    c0, c1, c2, c3, c4 = optimizer_params
    return float(c0) / np.power(iteration + 1 + c4, c2)


def get_c_spsa(iteration, optimizer_params):
    c0, c1, c2, c3, c4 = optimizer_params
    return float(c1) / np.power(iteration + 1, c3)


def initializeOptimization(n_thetas, optimizer_params):
    initial_thetas = np.random.default_rng().standard_normal(n_thetas)

    thetas_plus, thetas_minus, delta = generateDirections(0, initial_thetas, optimizer_params)
    return initial_thetas, thetas_plus, thetas_minus, delta


def computeProbabilities(results, is_statevector, n_data, n_classes, indices=None):
    """
        Compute probabilities from results
        results: either a list of qiskit.result.Result or one such object with multiple experiments
        indices: in the latter case: a list of the indices of the relevant experiments
    """
    circuit_id = 0
    predicted_probs = []
    predicted_labels = []
    counts = []
    for i in range(n_data):
        if is_statevector:
            if indices is not None:
                temp = results.get_statevector(
                    int(indices[i]))  # cast to int, otherwise int32 will not be recognized as int
            else:
                temp = results[i].get_statevector()
            outcome_vector = (temp * temp.conj()).real
            # convert outcome_vector to outcome_dict, where key
            # is a basis state and value is the count.
            # Note: the count can be scaled linearly, i.e.,
            # it does not have to be an integer.
            outcome_dict = {}
            bitstr_size = int(math.log2(len(outcome_vector)))
            for i, _ in enumerate(outcome_vector):
                bitstr_i = format(i, '0' + str(bitstr_size) + 'b')
                outcome_dict[bitstr_i] = outcome_vector[i]
        else:
            if indices is not None:
                outcome_dict = results.get_counts(int(indices[i]))
            else:
                outcome_dict = results[i].get_counts()

        counts.append(outcome_dict)
        circuit_id += 1

    probs = return_probabilities(counts, n_classes)
    predicted_probs.append(probs)
    predicted_labels.append(np.argmax(probs, axis=1))

    if len(predicted_probs) == 1:
        predicted_probs = predicted_probs[0]
    if len(predicted_labels) == 1:
        predicted_labels = predicted_labels[0]

    return predicted_probs, predicted_labels


def return_probabilities(counts, num_classes):
    probs = np.zeros(((len(counts), num_classes)))
    for idx in range(len(counts)):
        count = counts[idx]
        shots = sum(count.values())
        for k, v in count.items():
            label = assign_label(k, num_classes)
            probs[idx][label] += v / shots
    return probs


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
        total_size = 2 ** num_qubits
        class_step = np.floor(total_size / num_classes)

        decimal_value = measured_key.dot(1 << np.arange(measured_key.shape[-1] - 1, -1, -1))
        key_order = int(decimal_value / class_step)
        return key_order if key_order < num_classes else num_classes - 1


def cost_estimate(probs, gt_labels):
    mylabels = np.zeros(probs.shape)
    for i in range(gt_labels.shape[0]):
        whichindex = gt_labels[i]
        mylabels[i][whichindex] = 1

    x = cross_entropy(probs, mylabels)
    return x


def cross_entropy(predictions, targets, epsilon=1e-12):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    tmp = np.sum(targets * np.log(predictions), axis=1)
    ce = -np.sum(tmp) / N
    return ce


def generateCircuitTemplate(nqbits, reps_featuremap, reps_varform, entanglement, measure=False):
    """
        Generates the quantum circuit for variational SVM, which
        consists of a FeatureMap and the variational form.
        Fixed FeatureMap to ZFeatureMap instance and variational form
        to RyRz (for simplicity)
    """
    # instanciate feature map and variational form
    feature_map = ZFeatureMap(nqbits, reps_featuremap)
    var_form = TwoLocal(nqbits, ['ry', 'rz'], "cz", entanglement, reps_varform)

    # create empty circuit
    qr = QuantumRegister(nqbits, name='q')
    cr = ClassicalRegister(nqbits, name='c')
    qc = QuantumCircuit(qr, cr)

    # append feature map and variational form
    qc.append(feature_map.to_instruction(), qr)
    qc.append(var_form.to_instruction(), qr)

    # add measurements
    if measure:
        qc.barrier(qr)
        qc.measure(qr, cr)

    return qc, feature_map.parameters, var_form.parameters


def generateCircuitParameterizations(circuit, data: list, thetas: list):
    """
        Prepares the circuit parameterizations for the provided data points and thetas

            data: list of data points, shape N x d
                where   N = number of data points
                        d = dimension of data
            theta: list of trainable parameters, shape n x d
                with    n = number of parameterizations (with different set of thetas),
                        d = number of trainable parameters
    """
    fm_parameters, var_parameters = circuit[0][0].params, circuit[1][0].params
    fm_parameters, var_parameters = [param.name for param in fm_parameters], [param.name for param in var_parameters]

    parameterizations = []
    for theta in thetas:
        for datum in data:
            curr_params = dict(zip(fm_parameters, datum))
            curr_params.update(dict(zip(var_parameters, theta)))
            parameterizations.append(curr_params)

    return parameterizations


def runCircuit(circuit: QuantumCircuit, parameterizations: list, backend, token, shots, add_measurements=False):
    """
        Runs the circuit with each parameterization in the provided list and
        on the provided quantum instance and

        parameters
            - circuit: a QuantumCircuit to run
            - parameterizations: a list of dictionaries [parameter name] -> [value]
            - add_measurements: (optional) adds measurement operations if instance is not a statevector instance

        returns
            - results: a list of the results from these runs
            - is_statevector: True if QInstance is statevector
    """

    Qbackend = create_backend(backend, token)
    QInstance = QuantumInstance(Qbackend, seed_simulator=9283712, seed_transpiler=9283712, shots=shots)

    # add measurements
    if not QInstance.is_statevector and add_measurements:
        circuit.barrier()
        circuit.measure(circuit.qubits, circuit.clbits)

    circuits = []
    for parameterization in parameterizations:
        parameterization = parameterization_from_parameter_names(circuit, parameterization)
        curr_circuit = circuit.assign_parameters(parameterization)
        circuits.append(curr_circuit)

    results = QInstance.execute(circuits)

    return results


def parameterization_from_parameter_names(circuit, parameterization):
    """
        converts the dict [parameter name] -> [value] to
        [parameter] -> [value]
        i.e. replaces parameter names by actual parameters in circuit
    """

    parameters = circuit.parameters
    parameterization_new = {}
    for param_name in parameterization:
        for parameter in parameters:
            if parameter.name == param_name:
                parameterization_new[parameter] = parameterization[param_name]
                break
    return parameterization_new


def create_backend(backend_name, token=''):
    """
    Creates a quantum backend given the backend name.
    We allow two provider: aer, ibmq.
    We expect the backend_name to follow the format
    provider_instance
    i.e. ibmq_santiago, ibmq_16_melbourne, aer_qasm_simulator.
    """

    backend_name = backend_name.lower()
    if 'aer' in backend_name:
        provider = 'aer'
        instance = backend_name[4:]
    elif 'ibmq' in backend_name:
        provider = 'ibmq'
        instance = backend_name
    else:
        raise Exception('Unknown backend name specified.')

    if 'ibmq' in provider:
        if token == '':
            raise Exception('A token is needed when using ibm backends.')
        else:
            return IBMQ.enable_account(token).get_backend(instance)

    elif 'aer' in provider:
        if 'qasm' in instance:
            return Aer.get_backend('qasm_simulator')
        elif 'vector' in instance:
            return Aer.get_backend('statevector_simulator')
        else:
            raise Exception('Backend provider '
                            + provider
                            + ' does not have an instance called '
                            + instance
                            + '.')
    else:
        raise Exception('Unknown backend provider.')


async def fetch_data_as_text(session, url):
    async with session.get(url) as response:
        return await response.text()


async def download_to_file(url, file_path):
    async with aiohttp.ClientSession() as session:
        file = open(file_path, "w")
        content_as_text = await fetch_data_as_text(session, url)
        file.write(content_as_text)


def initialize_classification(data, entanglement, variational_form_reps, feature_map_reps,
                              optimizer_parameters):
    """
        Initialize variational SVM classification
        * generates circuit template
        * initializes optimization parameters
    """

    # use default parameters if not set
    if optimizer_parameters is None:
        print('Using default optimizer parameterization!')
        optimizer_parameters = default_optimizer_params

    # generate circuit template
    n_dimensions = data.shape[1]
    circuit_template, feature_map_parameters, var_form_parameters = generateCircuitTemplate(n_dimensions,
                                                                                            feature_map_reps,
                                                                                            variational_form_reps,
                                                                                            entanglement)

    # store circuit template
    # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
    circuit_template_pickle = pickle.dumps(circuit_template)

    # initialize thetas for optimization
    print('Initializing parameterization!')
    n_thetas = len(var_form_parameters)
    thetas, thetas_plus, thetas_minus, delta = initializeOptimization(n_thetas, optimizer_parameters)

    return circuit_template_pickle, thetas, thetas_plus, thetas_minus, delta


def generate_circuit_parameterizations(data, circuit_template_pickle, thetas, thetas_plus, thetas_minus):
    """
        Generate circuit parameterizations
        * takes circuit template, data, and thetas to generate parameterizations for the circuit execution
    """

    # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
    circuit_template = pickle.loads(circuit_template_pickle)

    thetas_array = []
    for t in [thetas, thetas_plus, thetas_minus]:
        if t is not None:
            thetas_array.append(t)

    # generate parameterizations
    return generateCircuitParameterizations(circuit_template, data, thetas_array)


def execute_circuits(circuit_template_pickle, parameterizations, backend_name, token, shots):
    """ Execute circuits """

    # deserialize inputs
    # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
    circuit_template = pickle.loads(circuit_template_pickle)

    # execute the circuits
    return runCircuit(circuit_template, parameterizations, backend_name, token, shots, add_measurements=True)


def optimize(results, labels, optimizer_parameters, thetas, delta, iteration, is_statevector):
    """
        Optimize parameters
        * evaluates the results from circuit execution
        * optimizes thetas using SPSA optimizer
        * generates thetas and delta for the next round (thetas_plus, thetas_minus)
    """

    if optimizer_parameters is None:
        print('Using default optimizer parameterization!')
        optimizer_parameters = default_optimizer_params

    # make that sure labels are integers
    labels = labels.astype(int)

    # optimize
    thetas_out, thetas_plus, thetas_minus, delta_out, costs_curr = optimize_results(results, labels, thetas, delta,
                                                                                    iteration,
                                                                                    optimizer_parameters,
                                                                                    is_statevector)

    return thetas_out, thetas_plus, thetas_minus, delta_out, costs_curr


async def train_classifier(data_url, label_url, maxiter, backend, token):
    print('Starting classification!')

    # temp files to store input data and labels from clustering
    data_file = tempfile.NamedTemporaryFile(delete=False)
    label_file = tempfile.NamedTemporaryFile(delete=False)

    # download the data and labels and store it locally
    await download_to_file(data_url, data_file.name)
    await download_to_file(label_url, label_file.name)

    # deserialize the data and labels
    data = np.loadtxt(data_file)
    labels = np.loadtxt(label_file)
    print(labels)

    """ Initialize """
    circuit_template, thetas, thetas_plus, thetas_minus, delta = initialize_classification(data, 'full', 3, 1, None)

    """ Optimize """
    print('Starting optimization loop!')
    for i in range(maxiter):
        print('Iteration: ' + str(i + 1))

        # get parameterization for current iteration
        parameterizations = generate_circuit_parameterizations(data, circuit_template, thetas, thetas_plus,
                                                               thetas_minus)
        print('Current parametrization: ', parameterizations)

        # run circuit with parametrization
        results = execute_circuits(circuit_template, parameterizations, backend, token, 1024)
        print('Circuits successfully executed!')

        # optimize based on execution results
        thetas, thetas_plus, thetas_minus, delta, costs_curr = optimize(results, labels, None, thetas, delta, i,
                                                                        'False')
        print('Current costs: ', costs_curr)

        # check if termination condition is met
        if costs_curr < 0.2:
            break

    print('Classification terminated!')
    return thetas


if __name__ == "__main__":
    thetas = asyncio.run(train_classifier(
        'https://raw.githubusercontent.com/UST-QuAntiL/QuantME-UseCases/scriptSplitting/TBD/data/subset-10_embeddings.txt',
        'https://raw.githubusercontent.com/UST-QuAntiL/QuantME-UseCases/scriptSplitting/TBD/data/subset-10_cluster-mappings.txt',
        20, 'aer_statevector_simulator', ''))
    print('Final thetas: ', thetas)
