"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

import numpy as np
from qiskit import *
from dataProcessingService import DataProcessingService
from quantumPostProcessingService import QuantumPostProcessingService


class ClusteringCircuitExecutor:
    """
    A class for executing clustering quantum circuits.
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
            hits = QuantumPostProcessingService.calculate_qubits_0_hits(histogram)

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
        cluster_mapping = DataProcessingService.calculate_cluster_mapping(amount_of_data, k, distances)

        return cluster_mapping

    @classmethod
    def execute_destructive_interference_clustering(cls, circuits, k, backend, shots_per_circuit):
        """
        Executes the given circuits for performing a destructive interference clustering.
        """

        # this is the amount of qubits that are needed in total
        # and also the amount of distances, i.e. every data point
        # to every centroid
        global_work_amount = 0
        for quantum_circuit in circuits:
            global_work_amount += quantum_circuit.num_qubits

        # store some general information about the data
        amount_of_data = int(global_work_amount / (2 + k))

        # we store the distances as [(t1,c1), (t1,c2), ..., (t1,cn), (t2,c1), ..., (tm,cn)]
        # while each (ti,cj) stands for one distance, i.e. (ti,cj) = distance data point i
        # to centroid j
        distances = np.zeros(int(global_work_amount / 2))

        # this is the index to iterate over all parameter pairs in the queue (parameters list)
        index = 0

        for quantum_circuit in circuits:
            # track the parameter pairs we will check within each circuit
            index += int(quantum_circuit.num_qubits / 2)

            # execute on IBMQ backend
            job = execute(quantum_circuit, backend, shots=shots_per_circuit)

            # store the result for this sub circuit run
            histogram = job.result().get_counts()
            hits = QuantumPostProcessingService.calculate_even_qubits_1_hits(histogram)

            # the amount of hits for the |1> state is proportional
            # to the distance. Using 1 data point and one centroid,
            # i.e. 2 qubits, P|11> + P|10> is proportional to the
            # distance (but not normed).
            for i in range(0, hits.shape[0]):
                distances[index - int(quantum_circuit.num_qubits / 2) + i] = hits[i]

        # calculate the new cluster mapping
        cluster_mapping = DataProcessingService.calculate_cluster_mapping(amount_of_data, k, distances)

        return cluster_mapping

    @classmethod
    def execute_state_preparation_clustering(cls, circuits, k, backend, shots_per_circuit):
        """
        Executes the given circuits for performing a state preparation clustering.
        """

        # this is the amount of qubits that are needed in total
        # and also the amount of distances, i.e. every data point
        # to every centroid
        global_work_amount = 0
        for quantum_circuit in circuits:
            global_work_amount += quantum_circuit.num_qubits

        # store some general information about the data
        amount_of_data = int(global_work_amount / (2 + k))

        # we store the distances as [(t1,c1), (t1,c2), ..., (t1,cn), (t2,c1), ..., (tm,cn)]
        # while each (ti,cj) stands for one distance, i.e. (ti,cj) = distance data point i
        # to centroid j
        distances = np.zeros(int(global_work_amount / 2))

        # this is the index to iterate over all parameter pairs in the queue (parameters list)
        index = 0

        for quantum_circuit in circuits:
            # track the parameter pairs we will check within each circuit
            index += int(quantum_circuit.num_qubits / 2)

            # execute on IBMQ backend
            job = execute(quantum_circuit, backend, shots=shots_per_circuit)

            # store the result for this sub circuit run
            histogram = job.result().get_counts()
            hits = QuantumPostProcessingService.calculate_even_qubits_0_hits(histogram)

            # the final state is entangled, i.e. P|00> = P|0X> = P|X0>
            # if using only 2 qubits. If using multiple qubits, we are
            # pairwise entangled. The amount of hits for the |0> state
            # is anti proportional to the distance. Using 1 data point
            # and one centroid, i.e. 2 qubits, P|0> is proportional to
            # - distance (but not normed)

            # we negate every hit and let the super class
            # calculate the centroid mapping according to the
            # minus distances.
            for i in range(0, hits.shape[0]):
                distances[index - int(quantum_circuit.num_qubits / 2) + i] = - hits[i]

        # calculate the new cluster mapping
        cluster_mapping = DataProcessingService.calculate_cluster_mapping(amount_of_data, k, distances)

        return cluster_mapping
