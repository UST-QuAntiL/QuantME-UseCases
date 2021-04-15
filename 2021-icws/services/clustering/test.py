"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

import matplotlib.pyplot as plt
import asyncio
from dataProcessingService import DataProcessingService
from fileService import FileService
import numpy as np
import requests
import json


def get_colors(k):
    """
    Return k colors in a list. We choose from 7 different colors.
    If k > 7 we choose colors more than once.
    """

    base_colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k']
    colors = []
    index = 1
    for i in range(0, k):
        if index % (len(base_colors) + 1) == 0:
            index = 1
        colors.append(base_colors[index - 1])
        index += 1
    return colors


def plot_data(data_lists, data_names, title, circle=False):
    """
    Plot all the data points with optional an unit circle.
    We expect to have data lists as a list of cluster points, i.e.
    data_lists =
    [ [ [x_0, y_0], [x_1, y_1], ... ], [x_0, y_0], [x_1, y_1], ... ] ]
    [      points of cluster 1       ,    points of cluster 2        ]
    data_names = [ "Cluster1", "Cluster2" ].
    """

    plt.clf()
    plt.figure(figsize=(7, 7), dpi=80)
    unit_circle_plot = plt.Circle((0, 0), 1.0, color='k', fill=False)
    ax = plt.gca()
    ax.cla()
    ax.set_xlim(-1.5, +1.5)
    ax.set_ylim(-1.5, +1.5)
    ax.set_title(title)
    if circle:
        ax.add_artist(unit_circle_plot)
    colors = get_colors(len(data_lists))
    for i in range(0, len(data_lists)):
        ax.scatter([data_points[0] for data_points in data_lists[i]],
                   [dataPoints[1] for dataPoints in data_lists[i]],
                   color=colors[i],
                   label=data_names[i])
    plt.show()
    return


def plot(data_raw, data, cluster_mapping, k):
    """
    Prepare data in order to plot.
    """

    data_texts = []
    clusters = dict()
    clusters_raw = dict()

    for i in range(0, cluster_mapping.shape[0]):
        cluster_number = int(cluster_mapping[i])
        if cluster_number not in clusters:
            clusters[cluster_number] = []
            clusters_raw[cluster_number] = []

        clusters[cluster_number].append(data[i])
        clusters_raw[cluster_number].append(data_raw[i])

    # add missing clusters that have no elements
    for i in range(0, k):
        if i not in clusters:
            clusters[i] = []

    clusters_plot = []
    clusters_raw_plot = []

    for i in range(0, k):
        clusters_plot.append([])
        clusters_raw_plot.append([])
        for j in range(0, len(clusters[i])):
            clusters_plot[i].append(clusters[i][j])
            clusters_raw_plot[i].append(clusters_raw[i][j])

    for i in range(0, k):
        data_texts.append("Cluster" + str(i))

    plot_data(clusters_plot, data_texts, "Preprocessed Data", circle=True)
    plot_data(clusters_raw_plot, data_texts, "Raw Data")


async def plot_data_from_urls(data_url, cluster_mapping_url, k):
    # create paths
    plot_folder_path = './static/test/plot/'
    data_file_path = plot_folder_path + 'data.txt'
    cluster_mapping_file_path = plot_folder_path + 'cluster_mapping.txt'

    # create folder and delete old files
    FileService.create_folder_if_not_exist(plot_folder_path)
    FileService.delete_if_exist(data_file_path, cluster_mapping_file_path)

    # download data
    await FileService.download_to_file(data_url, data_file_path)
    await FileService.download_to_file(cluster_mapping_url, cluster_mapping_file_path)

    # deserialize data
    data = np.loadtxt(data_file_path)
    cluster_mapping = np.loadtxt(cluster_mapping_file_path)

    # prepare plot data
    data_preprocessed = DataProcessingService.normalize(DataProcessingService.standardize(data))

    plot(data, data_preprocessed, cluster_mapping, k)


async def initialize_centroids(root_url, job_id, k):
    request_url = str(root_url) + '/api/centroid-calculation/initialization/' + str(job_id) + '?k=' + str(k)
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['centroids_url']


async def calculate_angles(root_url, job_id, data_url, centroids_url):
    request_url = str(root_url) + '/api/angle-calculation/rotational-clustering/' + str(job_id) + '?' + \
                  'data_url=' + str(data_url) + '&' + \
                  'centroids_url=' + str(centroids_url)
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['data_angles_url'], response['centroid_angles_url']


async def generate_quantum_circuits(root_url, job_id, data_angles_url, centroid_angles_url):
    request_url = str(root_url) + '/api/circuit-generation/negative-rotation-clustering/' + str(job_id) + '?' \
                                                                                                          'data_angles_url=' + str(
        data_angles_url) + '&' + \
                  'centroid_angles_url=' + str(centroid_angles_url)
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['circuits_url']


async def execute_quantum_circuits(root_url, job_id, circuits_url, k, backend_name):
    request_url = str(root_url) + '/api/circuit-execution/negative-rotation-clustering/' + str(job_id) + '?' + \
                  'circuits_url=' + str(circuits_url) + '&' + \
                  'k=' + str(k) + '&' + \
                  'backend_name=' + str(backend_name) + '&' + \
                  'token='
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['cluster_mapping_url']


async def calculate_centroids(root_url, job_id, data_url, cluster_mapping_url, old_centroids_url):
    request_url = str(root_url) + '/api/centroid-calculation/rotational-clustering/' + str(job_id) + '?' + \
                  'data_url=' + str(data_url) + '&' + \
                  'cluster_mapping_url=' + str(cluster_mapping_url) + '&' + \
                  'old_centroids_url=' + str(old_centroids_url)
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['centroids_url']


async def check_convergence(root_url, job_id, new_centroids_url, old_centroids_url, eps):
    request_url = str(root_url) + '/api/convergence-check/' + str(job_id) + '?' + \
                  'new_centroids_url=' + str(new_centroids_url) + '&' + \
                  'old_centroids_url=' + str(old_centroids_url) + '&' + \
                  'eps=' + str(eps)
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['convergence'], response['distance']


async def download_url_and_generate_temp_url(url_root, file_url, file_name):
    """
    Downloads the file on the given url and stores it locally.
    Also create for the locally stored file a url to access it.
    """

    test_folder_path = './static/test/'
    test_file_path = test_folder_path + str(file_name) + '.txt'
    FileService.create_folder_if_not_exist(test_folder_path)
    FileService.delete_if_exist(test_file_path)
    await FileService.download_to_file(file_url, test_file_path)
    return url_root + '/static/test/' + file_name + '.txt'


async def main():
    """
    This method tests the entire workflow within a python script.
    """

    # define main parameters
    k = 2
    job_id = 1
    eps = 0.001
    max_runs = 10
    url_root = 'http://127.0.0.1:5000'
    data_url = 'https://raw.githubusercontent.com/UST-QuAntiL/QuantME-UseCases/master/2021-icws/data/embedding.txt'
    backend_name = 'aer_qasm_simulator'
    print('Starting test script...')

    # call the task
    old_centroids_url = await initialize_centroids(url_root, job_id, k)
    print('URL of old centroids: ' + str(old_centroids_url))
    # safe the result from task locally
    old_centroids_local_url = await download_url_and_generate_temp_url(url_root, old_centroids_url, 'old_centroids')
    print('Initialized centroids and starting iterations...')

    for i in range(1, max_runs + 1):
        print('Running iteration: ' + str(i))

        # call the task
        data_angles_url, centroid_angles_url = await calculate_angles(
            url_root, job_id, data_url, old_centroids_local_url)
        print('Data angles URL: ' + data_angles_url)
        print('Centroid angles URL: ' + data_angles_url)

        # safe the result from task locally
        data_angles_local_url = await download_url_and_generate_temp_url(url_root, data_angles_url, 'data_angles')
        centroid_angles_local_url = await download_url_and_generate_temp_url(url_root, centroid_angles_url,
                                                                             'centroid_angles')

        # call the task
        circuits_url = await generate_quantum_circuits(
                url_root, job_id, data_angles_local_url, centroid_angles_local_url)

        # safe the result from task locally
        circuits_local_url = await download_url_and_generate_temp_url(url_root, circuits_url, 'circuits')
        cluster_mapping_url = await execute_quantum_circuits(
                url_root, job_id, circuits_local_url, k, backend_name)

        # safe the result from task locally
        cluster_mapping_local_url = await download_url_and_generate_temp_url(url_root, cluster_mapping_url,
                                                                             'cluster_mapping')

        # call the task
        new_centroids_url = await calculate_centroids(
            url_root, job_id, data_url, cluster_mapping_local_url, old_centroids_local_url)

        # safe the result from task locally
        new_centroids_local_url = await download_url_and_generate_temp_url(url_root, new_centroids_url, 'new_centroids')

        # call the task
        convergence, distance = await check_convergence(
            url_root, job_id, new_centroids_local_url, old_centroids_local_url, eps)

        # replace old centroids with new centroids
        old_centroids_local_url = new_centroids_local_url

        print('Iteration ' + str(i) + ' / ' + str(max_runs) + ' Distance = ' + str(distance))
        if convergence:
            print('Converged!')
            break

    # plot the results
    await plot_data_from_urls(data_url, cluster_mapping_local_url, k)


if __name__ == "__main__":
    asyncio.run(main())
