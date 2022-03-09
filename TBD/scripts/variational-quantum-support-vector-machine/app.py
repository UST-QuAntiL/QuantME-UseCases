import asyncio
import aiohttp
import pickle
import tempfile
import numpy as np
from qiskit.providers.aer import Aer
from qiskit.providers.ibmq import IBMQ
from qiskit import QuantumCircuit
from qiskit.utils import QuantumInstance
from variationalSVMCircuitGenerator import VariationalSVMCircuitGenerator
from SPSAOptimizer import SPSAOptimizer

default_optimizer_params = [0.6283185307179586, 0.1, 0.602, 0.101, 0]


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
    circuit_template, feature_map_parameters, var_form_parameters = \
        VariationalSVMCircuitGenerator.generateCircuitTemplate(n_dimensions, feature_map_reps,
                                                               variational_form_reps, entanglement)

    # store circuit template
    # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
    circuit_template_pickle = pickle.dumps(circuit_template)

    # initialize thetas for optimization
    print('Initializing parameterization!')
    n_thetas = len(var_form_parameters)
    thetas, thetas_plus, thetas_minus, delta = SPSAOptimizer.initializeOptimization(n_thetas, optimizer_parameters)

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
    return VariationalSVMCircuitGenerator.generateCircuitParameterizations(circuit_template, data,
                                                                           thetas_array)


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
    thetas_out, thetas_plus, thetas_minus, delta_out, costs_curr = SPSAOptimizer.optimize(results, labels, thetas,
                                                                                          delta, iteration,
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
