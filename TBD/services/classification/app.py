import sys
from quart import Quart, request, jsonify, Response
import asyncio
from fileService import FileService
from numpySerializer import NumpySerializer
from variationalSVMCircuitGenerator import VariationalSVMCircuitGenerator
from qiskitSerializer import QiskitSerializer
from SPSAOptimizer import SPSAOptimizer
from pickleSerializer import PickleSerializer
from circuitExecutor import CircuitExecutor
from listSerializer import ListSerializer
from resultsSerializer import ResultsSerializer
from decisionBoundaryPlotter import DecisionBoundaryPlotter

app = Quart(__name__)
app.config["DEBUG"] = False
loop = asyncio.get_event_loop()


def generate_url(url_root, route, file_name):
    return url_root + '/static/' + route + '/' + file_name + '.txt'


@app.route('/')
async def index():
    return 'QHana Classification Microservice'

@app.route('/api/variational-svm-classification/initialization/<int:job_id>', methods=['POST'])
async def initialize_classification(job_id):
    """
        Initialize variational SVM classification
        * generates circuit template
        * initializes optimization parameters
    """

    # response parameters
    message = 'success'
    status_code = 200

    # load the data from url or json body
    data_url = request.args.get('data-url', type=str)
    if data_url is None:
        data_url = (await request.get_json())['data-url']

    optimizer_parameters_url = request.args.get('optimizer-parameters-url', type=str)
    if optimizer_parameters_url is None:
        optimizer_parameters_url = (await request.get_json())['optimizer-parameters-url']

    entanglement = request.args.get('entanglement', type=str, default='full')
    feature_map_reps = request.args.get('feature-map-reps', type=int, default=1)
    variational_form_reps = request.args.get('variational-form-reps', type=int, default=3)

    # file paths (inputs)
    data_file_path = './static/variational-svm-classification/initialization/data' \
                     + str(job_id) + '.txt'
    optimizer_parameters_file_path = './static/variational-svm-classification/initialization/optimizer-parameters' \
                     + str(job_id) + '.txt'

    # file paths (outputs)
    circuit_template_file_path = './static/variational-svm-classification/initialization/circuit-template' \
                         + str(job_id) + '.txt'
    thetas_file_path = './static/variational-svm-classification/initialization/thetas' \
                         + str(job_id) + '.txt'
    thetas_plus_file_path = './static/variational-svm-classification/initialization/thetas-plus' \
                         + str(job_id) + '.txt'
    thetas_minus_file_path = './static/variational-svm-classification/initialization/thetas-minus' \
                         + str(job_id) + '.txt'
    delta_file_path = './static/variational-svm-classification/initialization/delta' \
                         + str(job_id) + '.txt'
    try:
        # create working folder if not exist
        FileService.create_folder_if_not_exist('./static/variational-svm-classification/initialization/')

        # delete old files if exist
        FileService.delete_if_exist(data_file_path,
                                    optimizer_parameters_file_path,
                                    circuit_template_file_path,
                                    thetas_file_path,
                                    thetas_plus_file_path,
                                    thetas_minus_file_path,
                                    delta_file_path)

        # download the data and store it locally
        await FileService.download_to_file(data_url, data_file_path)
        await FileService.download_to_file(optimizer_parameters_url, optimizer_parameters_file_path)

        # deserialize the data
        data = NumpySerializer.deserialize(data_file_path)

        # TODO: Make feature map and variational form selectable
        # generate circuit template
        n_dimensions = data.shape[1]
        circuit_template, feature_map_parameters, var_form_parameters = \
                VariationalSVMCircuitGenerator.generateCircuitTemplate(n_dimensions, feature_map_reps, variational_form_reps, entanglement)

        # store circuit template
        # TODO: Fix problems with deserialization, then use
        # circuit_template = QiskitSerializer.deserialize(circuit_template_file_path)
        # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
        PickleSerializer.serialize(circuit_template, circuit_template_file_path)

        # TODO: Optimizer initialization is still specific to SPSA optimizer -> generalize
        # deserialize optimizer parameters
        optimizer_parameters = NumpySerializer.deserialize(optimizer_parameters_file_path)
        if len(optimizer_parameters) is not 5:
            raise Exception("Wrong number of optimizer parameters. 5 parameters c0 through c4 expected.")

        # initialize thetas for optimization
        n_thetas = len(var_form_parameters)
        thetas, thetas_plus, thetas_minus, delta = SPSAOptimizer.initializeOptimization(n_thetas, optimizer_parameters)

        NumpySerializer.serialize(thetas, thetas_file_path)
        NumpySerializer.serialize(thetas_plus, thetas_plus_file_path)
        NumpySerializer.serialize(thetas_minus, thetas_minus_file_path)
        NumpySerializer.serialize(delta, delta_file_path)

        # generate urls
        url_root = request.host_url
        circuit_template_url = generate_url(url_root,
                                  'variational-svm-classification/initialization',
                                  'circuit-template' + str(job_id))
        thetas_url = generate_url(url_root,
                                  'variational-svm-classification/initialization',
                                  'thetas' + str(job_id))
        thetas_plus_url = generate_url(url_root,
                                  'variational-svm-classification/initialization',
                                  'thetas-plus' + str(job_id))
        thetas_minus_url = generate_url(url_root,
                                  'variational-svm-classification/initialization',
                                  'thetas-minus' + str(job_id))
        delta_url = generate_url(url_root,
                                  'variational-svm-classification/initialization',
                                  'delta' + str(job_id))


    except Exception as ex:
        message = str(ex)
        status_code = 500
        return jsonify(message=message, status_code=status_code)

    return jsonify(message=message,
                   status_code=status_code,
                   circuit_template_url=circuit_template_url,
                   thetas_url=thetas_url,
                   thetas_plus_url=thetas_plus_url,
                   thetas_minus_url=thetas_minus_url,
                   delta_url=delta_url)

@app.route('/api/variational-svm-classification/parameterization-generation/<int:job_id>', methods=['POST'])
async def generate_circuit_parameterizations(job_id):
    """
        Generate circuit parameterizations
        * takes circuit template, data, and thetas to generate parameterizations for the circuit execution
    """

    # response parameters
    message = 'success'
    status_code = 200

    # load the data from url or json body
    data_url = request.args.get('data-url', type=str)
    if data_url is None:
        data_url = (await request.get_json())['data-url']

    circuit_template_url = request.args.get('circuit-template-url', type=str)
    if circuit_template_url is None:
        circuit_template_url = (await request.get_json())['circuit-template-url']

    thetas_url = request.args.get('thetas-url', type=str)
    if thetas_url is None:
        thetas_url = (await request.get_json())['thetas-url']

    thetas_plus_url = request.args.get('thetas-plus-url', type=str)
    if thetas_plus_url is None:
        thetas_plus_url = (await request.get_json())['thetas-plus-url']

    thetas_minus_url = request.args.get('thetas-minus-url', type=str)
    if thetas_minus_url is None:
        thetas_minus_url = (await request.get_json())['thetas-minus-url']


    # file paths (inputs)
    data_file_path = './static/variational-svm-classification/circuit-generation/data' \
                     + str(job_id) + '.txt'
    circuit_template_file_path = './static/variational-svm-classification/circuit-generation/circuit-template' \
                     + str(job_id) + '.txt'
    thetas_file_path = './static/variational-svm-classification/circuit-generation/thetas' \
                     + str(job_id) + '.txt'
    thetas_plus_file_path = './static/variational-svm-classification/circuit-generation/thetas-plus' \
                     + str(job_id) + '.txt'
    thetas_minus_file_path = './static/variational-svm-classification/circuit-generation/thetas-minus' \
                     + str(job_id) + '.txt'

    # file paths (outputs)
    parameterizations_file_path = './static/variational-svm-classification/circuit-generation/parameterizations' \
                     + str(job_id) + '.txt'

    try:
        # create working folder if not exist
        FileService.create_folder_if_not_exist('./static/variational-svm-classification/circuit-generation/')

        # delete old files if exist
        FileService.delete_if_exist(data_file_path,
                                    circuit_template_file_path,
                                    thetas_file_path,
                                    thetas_plus_file_path,
                                    thetas_minus_file_path,
                                    parameterizations_file_path)

        # download and store locally
        await FileService.download_to_file(data_url, data_file_path)
        await FileService.download_to_file(circuit_template_url, circuit_template_file_path)

        if thetas_url is not None and thetas_url != '':
            await FileService.download_to_file(thetas_url, thetas_file_path)
        if thetas_plus_url is not None and thetas_plus_url != '':
            await FileService.download_to_file(thetas_plus_url, thetas_plus_file_path)
        if thetas_minus_url is not None and thetas_minus_url != '':
            await FileService.download_to_file(thetas_minus_url, thetas_minus_file_path)

        # deserialize inputs
        data = NumpySerializer.deserialize(data_file_path)

        # TODO: Fix problems with deserialization, then use
        # circuit_template = QiskitSerializer.deserialize(circuit_template_file_path)
        # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
        circuit_template = PickleSerializer.deserialize(circuit_template_file_path)

        thetas = NumpySerializer.deserialize(thetas_file_path) if thetas_url is not None and thetas_url != '' else None
        thetas_plus = NumpySerializer.deserialize(thetas_plus_file_path) if thetas_plus_url is not None and thetas_plus_url != '' else None
        thetas_minus = NumpySerializer.deserialize(thetas_minus_file_path) if thetas_minus_url is not None and thetas_minus_url != '' else None

        thetas_array = []
        for t in [thetas, thetas_plus, thetas_minus]:
            if t is not None:
                thetas_array.append(t)

        # generate parameterizations
        parameterizations = VariationalSVMCircuitGenerator.generateCircuitParameterizations(circuit_template, data, thetas_array)

        # serialize outputs
        ListSerializer.serialize(parameterizations, parameterizations_file_path)

        url_root = request.host_url
        parameterizations_url = generate_url(url_root,
                                  'variational-svm-classification/circuit-generation',
                                  'parameterizations' + str(job_id))

    except Exception as ex:
        message = str(ex)
        status_code = 500
        return jsonify(message=message, status_code=status_code)

    return jsonify(message=message,
                   status_code=status_code,
                   parameterizations_url=parameterizations_url)

@app.route('/api/variational-svm-classification/circuit-execution/<int:job_id>', methods=['POST'])
async def execute_circuits(job_id):
    """
        Execute circuits
        * assigns parameters of circuit template for each parameterization
        * runs the circuit for each parameterization
        * returns results as a list
    """

    # response parameters
    message = 'success'
    status_code = 200

    # load the data from url or json body
    circuit_template_url = request.args.get('circuit-template-url', type=str)
    if circuit_template_url is None:
        circuit_template_url = (await request.get_json())['circuit-template-url']

    parameterizations_url = request.args.get('parameterizations-url', type=str)
    if parameterizations_url is None:
        parameterizations_url = (await request.get_json())['parameterizations-url']

    backend_name = request.args.get('backend_name', type=str)
    if backend_name is None:
        backend_name = (await request.get_json())['backend_name']

    token = request.args.get('token', type=str)
    if token is None:
        token = (await request.get_json())['token']
    shots = request.args.get('shots', type=int, default=1024)

    # file paths (inputs)
    circuit_template_file_path = './static/variational-svm-classification/circuit-execution/circuit-template' \
                     + str(job_id) + '.txt'
    parameterizations_file_path = './static/variational-svm-classification/circuit-execution/parameterizations' \
                     + str(job_id) + '.txt'

    # file paths (outputs)
    results_file_path = './static/variational-svm-classification/circuit-execution/results' \
                     + str(job_id) + '.txt'

    try:
        # create working folder if not exist
        FileService.create_folder_if_not_exist('./static/variational-svm-classification/circuit-execution/')

        # delete old files if exist
        FileService.delete_if_exist(circuit_template_file_path,
                                    parameterizations_file_path,
                                    results_file_path)

        # download and store locally
        await FileService.download_to_file(circuit_template_url, circuit_template_file_path)
        await FileService.download_to_file(parameterizations_url, parameterizations_file_path)

        # deserialize inputs

        # TODO: Fix problems with deserialization, then use
        # circuit_template = QiskitSerializer.deserialize(circuit_template_file_path)
        # WORKAROUND until https://github.com/Qiskit/qiskit-terra/issues/5710 is fixed
        circuit_template = PickleSerializer.deserialize(circuit_template_file_path)

        parameterizations = ListSerializer.deserialize(parameterizations_file_path)

        results, is_statevector = CircuitExecutor.runCircuit(circuit_template, parameterizations, backend_name, token, shots, add_measurements=True)

        ResultsSerializer.serialize(results, results_file_path)
        url_root = request.host_url
        results_url = generate_url(url_root,
                                  'variational-svm-classification/circuit-execution',
                                  'results' + str(job_id))
    except Exception as ex:
        message = str(ex)
        status_code = 500
        return jsonify(message=message, status_code=status_code)


    return jsonify(message=message,
                   status_code=status_code,
                   results_url=results_url,
                   is_statevector=is_statevector)

@app.route('/api/variational-svm-classification/optimization/<int:job_id>', methods=['POST'])
async def optimize(job_id):
    """
        Optimize parameters
        * evaluates the results from circuit execution
        * optimizes thetas using SPSA optimizer
        * generates thetas and delta for the next round (thetas_plus, thetas_minus)
    """

    # response parameters
    message = 'success'
    status_code = 200

    # load the data from url or json body
    results_url = request.args.get('results-url', type=str)
    if results_url is None:
        results_url = (await request.get_json())['results-url']

    labels_url = request.args.get('labels-url', type=str)
    if labels_url is None:
        labels_url = (await request.get_json())['labels-url']

    thetas_in_url = request.args.get('thetas-url', type=str)
    if thetas_in_url is None:
        thetas_in_url = (await request.get_json())['thetas-url']

    delta_in_url = request.args.get('delta-url', type=str)
    if delta_in_url is None:
        delta_in_url = (await request.get_json())['delta-url']

    optimizer_parameters_url = request.args.get('optimizer-parameters-url', type=str)
    if optimizer_parameters_url is None:
        optimizer_parameters_url = (await request.get_json())['optimizer-parameters-url']

    iteration = request.args.get('iteration', type=int)
    if iteration is None:
        iteration = (await request.get_json())['iteration']

    is_statevector = request.args.get('is-statevector', type=str, default='False')
    is_statevector = False if is_statevector in ['False', '', 'No', 'None'] else True

    # file paths (inputs)
    results_file_path = './static/variational-svm-classification/optimization/results' \
                     + str(job_id) + '.txt'
    labels_file_path = './static/variational-svm-classification/optimization/labels' \
                     + str(job_id) + '.txt'
    thetas_in_file_path = './static/variational-svm-classification/optimization/thetas-in' \
                     + str(job_id) + '.txt'
    delta_in_file_path = './static/variational-svm-classification/optimization/delta-in' \
                     + str(job_id) + '.txt'
    optimizer_parameters_file_path = './static/variational-svm-classification/optimization/optimizer-parameters' \
                     + str(job_id) + '.txt'

    # file paths (inputs)
    thetas_out_file_path = './static/variational-svm-classification/optimization/thetas-out' \
                     + str(job_id) + '.txt'
    thetas_plus_file_path = './static/variational-svm-classification/optimization/thetas-plus' \
                     + str(job_id) + '.txt'
    thetas_minus_file_path = './static/variational-svm-classification/optimization/thetas-minus' \
                     + str(job_id) + '.txt'
    delta_out_file_path = './static/variational-svm-classification/optimization/delta-out' \
                     + str(job_id) + '.txt'

    try:
        # create working folder if not exist
        FileService.create_folder_if_not_exist('./static/variational-svm-classification/optimization/')

        # delete old files if exist
        FileService.delete_if_exist(results_file_path,
                                    labels_file_path,
                                    thetas_in_file_path,
                                    delta_in_file_path,
                                    optimizer_parameters_file_path,
                                    thetas_out_file_path,
                                    thetas_plus_file_path,
                                    thetas_minus_file_path,
                                    delta_out_file_path)

        # download and store locally
        await FileService.download_to_file(results_url, results_file_path)
        await FileService.download_to_file(labels_url, labels_file_path)
        await FileService.download_to_file(thetas_in_url, thetas_in_file_path)
        await FileService.download_to_file(delta_in_url, delta_in_file_path)
        await FileService.download_to_file(optimizer_parameters_url, optimizer_parameters_file_path)

        results = ResultsSerializer.deserialize(results_file_path)
        labels = NumpySerializer.deserialize(labels_file_path)
        thetas = NumpySerializer.deserialize(thetas_in_file_path)
        delta = NumpySerializer.deserialize(delta_in_file_path)
        optimizer_parameters = NumpySerializer.deserialize(optimizer_parameters_file_path)

        # make that sure labels are integers
        labels = labels.astype(int)

        thetas_out, thetas_plus, thetas_minus, delta_out, costs_curr = \
                SPSAOptimizer.optimize(results, labels, thetas, delta, iteration, optimizer_parameters, is_statevector)

        NumpySerializer.serialize(thetas_out, thetas_out_file_path)
        NumpySerializer.serialize(thetas_plus, thetas_plus_file_path)
        NumpySerializer.serialize(thetas_minus, thetas_minus_file_path)
        NumpySerializer.serialize(delta_out, delta_out_file_path)

        # generate urls
        url_root = request.host_url
        thetas_out_url = generate_url(url_root,
                                  'variational-svm-classification/optimization',
                                  'thetas-out' + str(job_id))
        thetas_plus_url = generate_url(url_root,
                                  'variational-svm-classification/optimization',
                                  'thetas-plus' + str(job_id))
        thetas_minus_url = generate_url(url_root,
                                  'variational-svm-classification/optimization',
                                  'thetas-minus' + str(job_id))
        delta_url = generate_url(url_root,
                                  'variational-svm-classification/optimization',
                                  'delta-out' + str(job_id))

    except Exception as ex:
        message = str(ex)
        status_code = 500
        return jsonify(message=message, status_code=status_code)


    return jsonify(message=message,
                   status_code=status_code,
                   thetas_out_url=thetas_out_url,
                   thetas_plus_url=thetas_plus_url,
                   thetas_minus_url=thetas_minus_url,
                   delta_url=delta_url,
                   costs_curr=costs_curr)

@app.route('/api/plots/grid-generation/<int:job_id>', methods=['POST'])
async def generate_grid(job_id):
    """
        Takes original data and generates a grid of new data points that surrounds original data
        - resolution parameter r determines the dimensions of the grid, e.g. r x r for 2 dimensional data 
    """

    # response parameters
    message = 'success'
    status_code = 200

    # load the data from url or json body
    data_url = request.args.get('data-url', type=str)
    if data_url is None:
        data_url = (await request.get_json())['data-url']

    resolution = request.args.get('resolution', type=int, default=50)

    # file paths (inputs)
    data_file_path = './static/plots/grid-generation/data' \
                     + str(job_id) + '.txt'

    # file paths (inputs)
    grid_file_path = './static/plots/grid-generation/grid' \
                     + str(job_id) + '.txt'

    try:
        # create working folder if not exist
        FileService.create_folder_if_not_exist('./static/plots/grid-generation/')

        # delete old files if exist
        FileService.delete_if_exist(data_file_path,
                                    grid_file_path)

        # download the data and store it locally
        await FileService.download_to_file(data_url, data_file_path)

        # deserialize the data
        data = NumpySerializer.deserialize(data_file_path)

        grid = DecisionBoundaryPlotter.generate_grid(data, resolution)

        NumpySerializer.serialize(grid, grid_file_path)

        # generate urls
        url_root = request.host_url
        grid_url = generate_url(url_root,
                                  'plots/grid-generation',
                                  'grid' + str(job_id))
    except Exception as ex:
        message = str(ex)
        status_code = 500
        return jsonify(message=message, status_code=status_code)

    return jsonify(message=message,
               status_code=status_code,
               grid_url=grid_url)

# TODO: Remove when QuantumCircuit serialization/deserialization is fixed

@app.route('/api/plots/prediction/<int:job_id>', methods=['POST'])
async def predict(job_id):
    """
        Predict
        * evaluates results and computes predictions from them
    """

    # response parameters
    message = 'success'
    status_code = 200

    # load the data from url or json body
    results_url = request.args.get('results-url', type=str)
    if results_url is None:
        results_url = (await request.get_json())['results-url']

    n_classes = request.args.get('n_classes', type=int, default=2)
    is_statevector = request.args.get('is-statevector', type=str, default='False')
    is_statevector = False if is_statevector in ['False', '', 'No', 'None'] else True

    # file paths (inputs)
    results_file_path = './static/plots/predictions/results' \
                     + str(job_id) + '.txt'

    # file paths (inputs)
    labels_file_path = './static/plots/predictions/labels' \
                     + str(job_id) + '.txt'

    try:
        # create working folder if not exist
        FileService.create_folder_if_not_exist('./static/plots/predictions/')

        # delete old files if exist
        FileService.delete_if_exist(results_file_path,
                                    labels_file_path)

        # download and store locally
        await FileService.download_to_file(results_url, results_file_path)

        results = ResultsSerializer.deserialize(results_file_path)

        labels = DecisionBoundaryPlotter.predict(results, n_classes, is_statevector)

        NumpySerializer.serialize(labels, labels_file_path)

        # generate urls
        url_root = request.host_url
        predictions_url = generate_url(url_root,
                                  'plots/predictions',
                                  'labels' + str(job_id))

    except Exception as ex:
        message = str(ex)
        status_code = 500
        return jsonify(message=message, status_code=status_code)


    return jsonify(message=message,
                   status_code=status_code,
                   predictions_url=predictions_url)

@app.route('/api/plots/plot/<int:job_id>', methods=['POST'])
async def plot_boundary(job_id):
    """
        Plots data and decision boundary
    """

    # response parameters
    message = 'success'
    status_code = 200

    # load the data from url or json body
    data_url = request.args.get('data-url', type=str)
    if data_url is None:
        data_url = (await request.get_json())['data-url']

    labels_url = request.args.get('labels-url', type=str)
    if labels_url is None:
        labels_url = (await request.get_json())['labels-url']

    grid_url = request.args.get('grid-url', type=str)
    if grid_url is None:
        grid_url = (await request.get_json())['grid-url']

    predicitons_url = request.args.get('predictions-url', type=str)
    if predicitons_url is None:
        predicitons_url = (await request.get_json())['predictions-url']

    # file paths (inputs)
    data_file_path = './static/plots/plot/data' \
                     + str(job_id) + '.txt'

    labels_file_path = './static/plots/plot/labels' \
                     + str(job_id) + '.txt'

    grid_file_path = './static/plots/plot/grid' \
                     + str(job_id) + '.txt'

    predictions_file_path = './static/plots/plot/predictions' \
                     + str(job_id) + '.txt'

    # file paths (outputs)
    plot_file_path = './static/plots/plot/plot' \
                         + str(job_id) + '.png'

    try:
        # create working folder if not exist
        FileService.create_folder_if_not_exist('./static/plots/plot/')

        # delete old files if exist
        FileService.delete_if_exist(data_file_path,
                                    labels_file_path,
                                    grid_file_path,
                                    predictions_file_path,
                                    plot_file_path)

        # download the data and store it locally
        await FileService.download_to_file(data_url, data_file_path)
        await FileService.download_to_file(labels_url, labels_file_path)
        await FileService.download_to_file(grid_url, grid_file_path)
        await FileService.download_to_file(predicitons_url, predictions_file_path)

        # deserialize the data
        data = NumpySerializer.deserialize(data_file_path)
        labels = NumpySerializer.deserialize(labels_file_path)
        grid = NumpySerializer.deserialize(grid_file_path)
        predictions = NumpySerializer.deserialize(predictions_file_path)

        labels = labels.astype(int)
        predictions = predictions.astype(int)

        DecisionBoundaryPlotter.save_plot(data, labels, grid, predictions, plot_file_path)

        # generate urls
        url_root = request.host_url
        plot_url = url_root + '/static/plots/plot/plot' + str(job_id) + '.png'

    except Exception as ex:
        message = str(ex)
        status_code = 500
        return jsonify(message=message, status_code=status_code)

    return jsonify(message=message,
                   status_code=status_code,
                   plot_url=plot_url)

@app.route('/static/variational-svm-classification/initialization/circuit-template<int:job_id>.txt', methods=['GET'])
async def get_pickle_circuit(job_id):
    payload = open('./static/variational-svm-classification/initialization/circuit-template' + str(job_id) + '.txt', 'rb').read()
    content_type = 'application/python-pickle'
    return Response(response=payload, mimetype=content_type)

if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except Exception as ex:
        print("Usage: {} <port>".format(sys.argv[0]))
        exit()
    loop.run_until_complete(app.run_task(host="0.0.0.0", port=port))