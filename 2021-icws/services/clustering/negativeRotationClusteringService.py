"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

import numpy as np
from qiskit import *


class NegativeRotationClusteringService:
    """
    A class for performing a negative rotation clustering
    """

    @classmethod
    def execute_negative_rotation_clustering(cls, circuits, k, backend, shots_per_circuit):
        """
        Executes the given circuits for performing a negative rotation clustering.
        """

        # this is the amount of qubits that are needed in total
        # and also the amount of distances, i.e. every data point
        # to every centroid
        global_work_amount = 0
        for quantum_circuit in circuits:
            global_work_amount += quantum_circuit.num_qubits

        # store some general information about the data
        amount_of_data = int(global_work_amount / k)

        # we store the distances as [(t1,c1), (t1,c2), ..., (t1,cn), (t2,c1), ..., (tm,cn)]
        # while each (ti,cj) stands for one distance, i.e. (ti,cj) = distance data point i
        # to centroid j
        distances = np.zeros(global_work_amount)

        # this is the index to iterate over all parameter pairs in the queue (parameters list)
        index = 0

        for quantum_circuit in circuits:
            # track the parameter pairs we will check within each circuit
            index += quantum_circuit.num_qubits

            # execute on IBMQ backend
            job = execute(quantum_circuit, backend, shots=shots_per_circuit)

            # store the result for this sub circuit run
            histogram = job.result().get_counts()
            hits = cls.calculate_qubits_0_hits(histogram)

            # We will assign the data point to the centroid
            # with more 0 hits. E.g. if k = 2 we have hits
            # for the comparison with the first and second
            # centroid. The higher the hits, the closer we
            # are, i.e. the lower the distance. I.e. the
            # hit amount is anti proportional to the distance.
            # Hence, we add a small amount to each hit (to avoid
            # zero division) and take the inverse of it and
            # let the super class calculate the mapping, which
            # will assign to the centroid with minimal distance.
            safe_delta = 50
            for i in range(0, hits.shape[0]):
                distances[index - quantum_circuit.num_qubits + i] = 1.0 / (hits[i] + safe_delta)

        # calculate the new cluster mapping
        cluster_mapping = cls.calculate_cluster_mapping(amount_of_data, k, distances)

        return cluster_mapping

    @classmethod
    def calculate_cluster_mapping(cls, amount_of_data, k, distances):
        """
        Calculates the cluster mapping given the distances.
        I.e. we take the amount of data, k and the distances and create the
        mapping from data point to centroid, i.e. per data point we associate
        the centroid with the shortest distance. We suppose the distances
        to be in the format distance_i = [dist i to c1, dist i to c2, ...]

        We return a list with a mapping from data point indices to centroid indices,
        i.e. if we return a list [2, 0, 1, ...] this means:

        data vector with index 0 -> mapped to centroid with index 2
        data vector with index 1 -> mapped to centroid 0
        data vector with index 2 -> mapped to centroid 1
        ...
        """

        cluster_mapping = np.zeros(amount_of_data)
        for i in range(0, amount_of_data):
            lowest_distance = distances[i * k + 0]
            lowest_distance_centroid_index = 0
            for j in range(1, k):
                if distances[i * k + j] < lowest_distance:
                    lowest_distance_centroid_index = j
            cluster_mapping[i] = lowest_distance_centroid_index

        return cluster_mapping

    @classmethod
    def map_histogram_to_qubit_hits(cls, histogram):
        """
        Maps the histogram (dictionary) to a 2D np.array with the format
        qubit_i = [#hits |0>, #hits |1>].
        """

        # create array and store the hits per qubit, i.e. [#|0>, #|1>]
        length = int(len(list(histogram.keys())[0]))
        qubit_hits = np.zeros((length, 2))

        for basis_state in histogram:
            for i in range(0, length):
                if basis_state[length - i - 1] == '0':
                    qubit_hits[i][0] = qubit_hits[i][0] + histogram[basis_state]
                else:
                    qubit_hits[i][1] = qubit_hits[i][1] + histogram[basis_state]

        return qubit_hits

    @classmethod
    def calculate_qubits_0_hits(cls, histogram):
        """
        Calculates for all qubits how often they hit the
        |0> state. We use the format qubit_i = #hits|0>.
        """

        # the length can be read out from the
        # string of any arbitrary (e.g. the 0th) bitstring
        length = int(len(list(histogram.keys())[0]))
        hits = np.zeros(length)

        qubit_hits_map = cls.map_histogram_to_qubit_hits(histogram)
        for i in range(0, int(qubit_hits_map.shape[0])):
            hits[i] = int(qubit_hits_map[i][0])

        return hits
