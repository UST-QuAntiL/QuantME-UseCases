"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

import numpy as np


class NumpySerializer:
    """
    A class for serializing numpy arrays.
    """

    @staticmethod
    def serialize(array, file_path):
        """
        Serializes the given numpy array and stores it
        at the given location.
        """

        np.savetxt(file_path, array)

    @staticmethod
    def deserialize(file_path):
        """
        Deserializes the file behind the given url
        to a numpy array.
        """

        return np.loadtxt(file_path)
