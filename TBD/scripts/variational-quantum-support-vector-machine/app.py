import asyncio
import pickle
import tempfile
from fileService import FileService
from serializers.numpySerializer import NumpySerializer
from variationalSVMCircuitGenerator import VariationalSVMCircuitGenerator
from SPSAOptimizer import SPSAOptimizer
from circuitExecutor import CircuitExecutor
from serializers.resultsSerializer import ResultsSerializer

default_optimizer_params = [0.6283185307179586, 0.1, 0.602, 0.101, 0]


async def initialize_classification(data, entanglement, variational_form_reps, feature_map_reps,
                                    optimizer_parameters):
    """
        Initialize variational SVM classification
        * generates circuit template
        * initializes optimization parameters
    """

    # use default parameters if not set
    if optimizer_parameters is None:
        print('Using default parameterization!')
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


async def generate_circuit_parameterizations(data, circuit_template_pickle, thetas, thetas_plus, thetas_minus):
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
    parameterizations = VariationalSVMCircuitGenerator.generateCircuitParameterizations(circuit_template, data,
                                                                                        thetas_array)

    return parameterizations


async def execute_circuits(circuit_template_pickle, parameterizations, backend_name, token, shots):
    """
        Execute circuits
        * assigns parameters of circuit template for each parameterization
        * runs the circuit for each parameterization
        * returns results as a list
    """

    # deserialize inputs
    # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
    circuit_template = pickle.loads(circuit_template_pickle)

    # execute the circuits
    results = CircuitExecutor.runCircuit(circuit_template, parameterizations, backend_name, token,
                                         shots, add_measurements=True)
    result_file = tempfile.NamedTemporaryFile(delete=False)
    ResultsSerializer.serialize(results, result_file.name)
    return ResultsSerializer.deserialize(result_file.name)


async def optimize(results, labels, optimizer_parameters, thetas, delta, iteration, is_statevector):
    """
        Optimize parameters
        * evaluates the results from circuit execution
        * optimizes thetas using SPSA optimizer
        * generates thetas and delta for the next round (thetas_plus, thetas_minus)
    """

    if optimizer_parameters is None:
        print('Using default parameterization!')
        optimizer_parameters = default_optimizer_params

    # make that sure labels are integers
    labels = labels.astype(int)

    # optimize
    thetas_out, thetas_plus, thetas_minus, delta_out, costs_curr = SPSAOptimizer.optimize(results, labels, thetas,
                                                                                          delta, iteration,
                                                                                          optimizer_parameters,
                                                                                          is_statevector)

    return thetas_out, thetas_plus, thetas_minus, delta_out, costs_curr


async def classify(data_url, label_url, maxiter, backend, token):
    print('Starting classification!')

    # temp files to store input data and labels from clustering
    data_file = tempfile.NamedTemporaryFile(delete=False)
    label_file = tempfile.NamedTemporaryFile(delete=False)

    # download the data and labels and store it locally
    await FileService.download_to_file(data_url, data_file.name)
    await FileService.download_to_file(label_url, label_file.name)

    # deserialize the data and labels
    data = NumpySerializer.deserialize(data_file)
    labels = NumpySerializer.deserialize(label_file)
    print(labels)

    """ Initialize """
    circuit_template, thetas, thetas_plus, thetas_minus, delta = await initialize_classification(data, 'full', 3, 1,
                                                                                                 None)

    """ Optimize """
    print('Starting optimization loop!')
    for i in range(maxiter):
        print('Iteration: ' + str(i + 1))

        # get parameterization for current iteration
        parameterizations = await generate_circuit_parameterizations(data, circuit_template, thetas, thetas_plus,
                                                                     thetas_minus)
        print('Current parametrization: ', parameterizations)

        # run circuit with parametrization
        results = await execute_circuits(circuit_template, parameterizations, backend, token, 1024)
        print('Circuits successfully executed!')

        # optimize based on execution results
        thetas, thetas_plus, thetas_minus, delta, costs_curr = await optimize(results, labels, None, thetas, delta, i,
                                                                              'False')

        # check if termination condition is met
        if costs_curr < 0.2:
            break

    print('Classification terminated!')
    return thetas


if __name__ == "__main__":
    thetas = asyncio.run(classify(
        'https://raw.githubusercontent.com/UST-QuAntiL/QuantME-UseCases/scriptSplitting/TBD/data/subset-10_embeddings.txt',
        'https://raw.githubusercontent.com/UST-QuAntiL/QuantME-UseCases/scriptSplitting/TBD/data/subset-10_cluster-mappings.txt',
        20, 'aer_statevector_simulator', ''))
    print('Final thetas: ', thetas)
