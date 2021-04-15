"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

from qiskit import QuantumCircuit


class ClusteringCircuitGenerator:
    """
    A class for generating clustering quantum circuits.
    """

    @classmethod
    def generate_negative_rotation_clustering(cls, max_qubits, data_angles, centroid_angles):
        """
        Generate the circuits for performing a negative rotation clustering.
        We take data and the centroid angles and generate Qiskit quantum
        circuits under consideration of the maximum amount of qubits.

        The data need to be in 1D cartesian representation in an
        np.array of shape = (amount) while the length of centroid angles
        is k.

        We return a list of Qiskit Quantum Circuits with each having at maximum
        max_qubits Qubits.
        """

        # store a list of quantum circuits
        circuits = []

        # this is also the amount of qubits that are needed in total
        # note that this is not necessarily in parallel, also sequential
        # is possible here
        global_work_amount = centroid_angles.shape[0] * data_angles.shape[0]

        # create tuples of parameters corresponding for each qubit,
        # i.e. create [[t1,c1], [t1,c2], ..., [t1,cn], [t2,c1], ..., [tm,cn]]
        # now with ti = data_angle_i and cj = centroid_angle_j
        parameters = []
        for i in range(0, data_angles.shape[0]):
            for j in range(0, centroid_angles.shape[0]):
                parameters.append((data_angles[i], centroid_angles[j]))

        # this is the index to iterate over all parameter pairs in the queue (parameters list)
        index = 0
        queue_not_empty = True

        # create the circuit(s)
        while queue_not_empty:
            max_qubits_for_circuit = global_work_amount - index

            if max_qubits < max_qubits_for_circuit:
                qubits_for_circuit = max_qubits
            else:
                qubits_for_circuit = max_qubits_for_circuit

            qc = QuantumCircuit(qubits_for_circuit, qubits_for_circuit)

            for i in range(0, qubits_for_circuit):
                # test_angle rotation
                qc.ry(parameters[index][0], i)

                # negative centroid_angle rotation
                qc.ry(-parameters[index][1], i)

                # measure
                qc.measure(i, i)

                index += 1
                if index == global_work_amount:
                    queue_not_empty = False
                    break

            circuits.append(qc)

        return circuits

