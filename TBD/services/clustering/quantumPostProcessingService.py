"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

import numpy as np


class QuantumPostProcessingService:
    """
    A service class for post processing of quantum experiments.
    """

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

    @classmethod
    def calculate_qubits_1_hits(cls, histogram):
        """
        Calculates for all qubits how often they hit the
        |1> state. We use the format qubit_i = #hits|1>.
        """

        # the length can be read out from the
        # string of any arbitrary (e.g. the 0th) bitstring
        length = int(len(list(histogram.keys())[0]))
        hits = np.zeros(length)

        qubit_hits_map = cls.map_histogram_to_qubit_hits(histogram)
        for i in range(0, int(qubit_hits_map.shape[0])):
            hits[i] = int(qubit_hits_map[i][1])

        return hits

    @classmethod
    def calculate_odd_qubits_0_hits(cls, histogram):
        """
        Calculates for all odd qubits how often they hit the
        |0> state. We use the format odd_qubit_i = #hits|0>.
        """

        qubits_0_hits = cls.calculate_qubits_0_hits(histogram)
        length = qubits_0_hits.shape[0]

        # if we have even many qubits, we have 1/2 odds
        # if we have odd many qubits, we still have 1/2 odds
        length /= 2

        length = int(length)
        hits = np.zeros(length)

        for i in range(0, length):
            hits[i] = int(qubits_0_hits[i * 2 + 1])

        return hits

    @classmethod
    def calculate_odd_qubits_1_hits(cls, histogram):
        """
        Calculates for all odd qubits how often they hit the
        |1> state. We use the format [odd_qubit_i, #hits|1>].
        """

        qubits_1_hits = cls.calculate_qubits_1_hits(histogram)
        length = qubits_1_hits.shape[0]

        # if we have even many qubits, we have 1/2 odds
        # if we have odd many qubits, we still have 1/2 odds
        length /= 2

        length = int(length)
        hits = np.zeros(length)

        for i in range(0, length):
            hits[i] = int(qubits_1_hits[i * 2 + 1])

        return hits

    @classmethod
    def calculate_even_qubits_0_hits(cls, histogram):
        """
        Calculates for all even qubits how often they hit the
        |0> state. We use the format even_qubit_i = #hits|0>.
        """

        qubits_0_hits = cls.calculate_qubits_0_hits(histogram)
        length = qubits_0_hits.shape[0]

        # if we have even many qubits, we have 1/2 even
        # if we have odd many qubits, we have 1/2 + 1 even
        if length % 2 == 1:
            length /= 2
            length += 1
        else:
            length /= 2

        length = int(length)
        hits = np.zeros(length)

        for i in range(0, length):
            hits[i] = int(qubits_0_hits[i * 2])

        return hits

    @classmethod
    def calculate_even_qubits_1_hits(cls, histogram):
        """
        Calculates for all even qubits how often they hit the
        |1> state. We use the format even_qubit_i = #hits|1>.
        """

        qubits_1_hits = cls.calculate_qubits_1_hits(histogram)
        length = qubits_1_hits.shape[0]

        # if we have even many qubits, we have 1/2 even
        # if we have odd many qubits, we have 1/2 + 1 even
        if length % 2 == 1:
            length /= 2
            length += 1
        else:
            length /= 2

        length = int(length)
        hits = np.zeros(length)

        for i in range(0, length):
            hits[i] = int(qubits_1_hits[i * 2])

        return hits
