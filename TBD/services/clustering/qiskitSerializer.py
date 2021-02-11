"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

from qiskit import QuantumCircuit


qasm_file_separator_token = '##########'


class QiskitSerializer:
    """
    A class for serializing Qiskit Quantum Circuits.
    """

    @staticmethod
    def serialize(circuits, file_path):
        """
        Serializes the given Qiskit Quantum Circuits and stores it
        at the given location.
        """

        with open(file_path, 'a') as file:
            for i in range(0, len(circuits)):
                file.write(circuits[i].qasm())
                if i != len(circuits) - 1:
                    file.write(qasm_file_separator_token + '\n')

    @staticmethod
    def deserialize(file_path):
        """
        Deserializes the file behind the given url
        to list of Qiskit Quantum Circuits.
        """

        with open(file_path, 'r') as file:
            circuits_strings = file.read().split(qasm_file_separator_token)

        # store the circuits in a list
        circuits = []

        for circuit_string in circuits_strings:
            circuits.append(QuantumCircuit.from_qasm_str(circuit_string))

        return circuits
