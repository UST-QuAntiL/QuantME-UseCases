import aiohttp
from cached_property import asyncio
import matplotlib.pyplot as plt
import json
import requests
import webbrowser

async def initialize_varSVM(url_root, job_id, data_url, optimizer_parameters_url):
    request_url = url_root + '/api/variational-svm-classification/initialization/' +\
                                str(job_id) +\
                                '?data-url=' + data_url +\
                                '&optimizer-parameters-url=' + optimizer_parameters_url
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['circuit_template_url'],\
            response['thetas_url'],\
            response['thetas_plus_url'],\
            response['thetas_minus_url'],\
            response['delta_url']

async def generate_parameterizations_varSVM(url_root, job_id, data_url, circuit_template_url, thetas_url, thetas_plus_url, thetas_minus_url):
    request_url = url_root + '/api/variational-svm-classification/parameterization-generation/' +\
                                str(job_id) +\
                                '?data-url=' + data_url +\
                                '&circuit-template-url=' + circuit_template_url +\
                                '&thetas-url=' + thetas_url +\
                                '&thetas-plus-url=' + thetas_plus_url +\
                                '&thetas-minus-url=' + thetas_minus_url
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['parameterizations_url']

async def run_circuit_parameterizations(url_root, job_id, circuit_template_url, parameterizations_url, backend, token):
    request_url = url_root + '/api/variational-svm-classification/circuit-execution/' +\
                                str(job_id) +\
                                '?circuit-template-url=' + circuit_template_url +\
                                '&parameterizations-url=' + parameterizations_url +\
                                '&backend_name=' + backend +\
                                '&token=' + token
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['results_url'],\
            response['is_statevector']

async def optimize_varSVM(url_root, job_id, results_url, labels_url, thetas_url, delta_url, optimizer_parameters_url, iteration, is_statevector):
    request_url = url_root + '/api/variational-svm-classification/optimization/' +\
                                str(job_id) +\
                                '?results-url=' + results_url +\
                                '&labels-url=' + labels_url +\
                                '&thetas-url=' + thetas_url +\
                                '&delta-url=' + delta_url +\
                                '&optimizer-parameters-url=' + optimizer_parameters_url +\
                                '&is-statevector=' + str(is_statevector) +\
                                '&iteration=' + str(iteration)
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['thetas_out_url'],\
            response['thetas_plus_url'],\
            response['thetas_minus_url'],\
            response['delta_url'],\
            response['costs_curr']

async def generate_grid(url_root, data_url, job_id, resolution):
    request_url = url_root + '/api/plots/grid-generation/' +\
                                str(job_id) +\
                                '?data-url=' + data_url +\
                                '&resolution=' + str(resolution)
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['grid_url']

async def compute_predictions(url_root, job_id, results_url, is_statevector):
    request_url = url_root + '/api/plots/prediction/' +\
                                str(job_id) +\
                                '?results-url=' + results_url +\
                                '&is-statevector=' + str(is_statevector)
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['predictions_url']

async def plot_boundary(url_root, job_id, data_url, labels_url, grid_url, predictions_url):
    request_url = url_root + '/api/plots/plot/' +\
                                str(job_id) +\
                                '?data-url=' + data_url +\
                                '&labels-url=' + labels_url +\
                                '&grid-url=' + grid_url +\
                                '&predictions-url=' + predictions_url
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['plot_url']

async def plot_costs(costs):
    plt.plot(costs)
    plt.show()

async def test_varSVM():
    """ test variational SVM classification workflow """

    maxiter = 20
    url_root = 'http://127.0.0.1:5001'
    data_url = url_root + '/static/0_base/embedding0.txt'
    labels_url = url_root + '/static/0_base/labels0.txt'
    optimizer_parameters_url = url_root + '/static/0_base/optimizer-parameters.txt'
    backend = 'aer_statevector_simulator'
    token = ''
    resolution = 25

    job_id = 0

    """ Initialize """
    circuit_template_url, thetas_url, thetas_plus_url, thetas_minus_url, delta_url = \
            await initialize_varSVM(url_root,\
                                    job_id,\
                                    data_url,\
                                    optimizer_parameters_url)

    """ Optimize """
    costs = []
    for i in range(maxiter):
        # generate parameterizations
        parameterizations_url = \
                await generate_parameterizations_varSVM(url_root,\
                                                        job_id, data_url,\
                                                        circuit_template_url,\
                                                        '',\
                                                        thetas_plus_url,\
                                                        thetas_minus_url)

        # run circuit with parameterizations
        results_url, is_statevector = \
                await run_circuit_parameterizations(url_root,\
                                                    job_id,\
                                                    circuit_template_url,\
                                                    parameterizations_url,\
                                                    backend,\
                                                    token)

        thetas_url, thetas_plus_url, thetas_minus_url, delta_url, costs_curr = \
                await optimize_varSVM(url_root,\
                                      job_id,\
                                      results_url,\
                                      labels_url,\
                                      thetas_url,\
                                      delta_url,\
                                      optimizer_parameters_url,\
                                      i+1,\
                                      is_statevector)

        costs.append(costs_curr)
        job_id+=1

        if costs_curr < 0.2:
            break

    """ Create plot(s) """
    grid_url = await generate_grid(url_root, data_url, job_id, resolution)

    parameterizations_url = \
                await generate_parameterizations_varSVM(url_root,\
                                                        job_id, grid_url,\
                                                        circuit_template_url,\
                                                        thetas_url,\
                                                        '',\
                                                        '')
    results_url, is_statevector = \
                await run_circuit_parameterizations(url_root,\
                                                    job_id,\
                                                    circuit_template_url,\
                                                    parameterizations_url,\
                                                    backend,\
                                                    token)

    predictions_url = await compute_predictions(url_root,\
                                           job_id,\
                                           results_url,\
                                           is_statevector)

    plot_url = await plot_boundary(url_root,\
                                   job_id,\
                                   data_url,\
                                   labels_url,\
                                   grid_url,\
                                   predictions_url)

    webbrowser.open(plot_url)
    await plot_costs(costs)

if __name__ == '__main__':
    asyncio.run(test_varSVM())