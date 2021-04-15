"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

import numpy as np
from math import acos, sqrt
import random


class DataProcessingService:
    """
    A service class for all kind of data processing functions
    like angle calculation, centroid calculation, normalization,
    standardization, etc.
    """

    @classmethod
    def generate_random_data(cls, amount):
        """
        Generate amount many random 2D data points and store
        it as np.array with shape = (amount, 2).
        """

        data = np.zeros((amount, 2))

        # create random float numbers per coordinate
        for i in range(0, amount):
            data[i][0] = random.uniform(-1.0, 1.0)
            data[i][1] = random.uniform(-1.0, 1.0)

        return data

    @classmethod
    def standardize(cls, data):
        """
        Standardize all the 2D points given in the data np.array,
        i.e. all the points will have zero mean and unit variance.
        We expect the np.array to represent a matrix with the
        coordinates of point i being data[i] = [x, y].
        Note that a copy of the data points will be created.
        """

        # create empty arrays
        data_x = np.zeros(data.shape[0])
        data_y = np.zeros(data.shape[0])
        preprocessed_data = np.zeros_like(data)

        # create x and y coordinate arrays
        for i in range(0, len(data)):
            data_x[i] = data[i][0]
            data_y[i] = data[i][1]

        # make zero mean and unit variance, i.e. standardize
        temp_data_x = (data_x - np.mean(data_x)) / np.std(data_x)
        temp_data_y = (data_y - np.mean(data_y)) / np.std(data_y)

        # create tuples to return
        for i in range(0, data.shape[0]):
            preprocessed_data[i][0] = temp_data_x[i]
            preprocessed_data[i][1] = temp_data_y[i]

        return preprocessed_data

    @classmethod
    def normalize(cls, data):
        """
        Normalize the 2D data, i.e. every entry of data has length 1.
        We expect the np.array to represent a matrix with the
        coordinates of point i being data[i] = [x, y].
        Note that a copy of the data points will be created.
        """

        preprocessed_data = np.zeros_like(data)

        # create tuples and normalize
        for i in range(0, data.shape[0]):
            norm = sqrt(pow(data[i][0], 2) + pow(data[i][1], 2))
            preprocessed_data[i][0] = data[i][0] / norm
            preprocessed_data[i][1] = data[i][1] / norm

        return preprocessed_data

    @classmethod
    def calculate_angles(cls, cartesian_points, base_vector):
        """
        Calculates the angles between the 2D vectors and the given 2D base vector.
        """

        angles = np.zeros(cartesian_points.shape[0])
        for i in range(0, angles.shape[0]):
            # formula: alpha = acos( 1/(|a||b|) * a • b )
            # here: |a| = |b| = 1
            angles[i] = acos(
                base_vector[0] * cartesian_points[i][0] + base_vector[1] * cartesian_points[i][1])

        return angles

    @classmethod
    def calculate_centroids(cls, cluster_mapping, old_centroids, data):
        """
        Calculates the new cartesian positions of the
        given centroids in the cluster mapping.
        Note that a copy of the data points will be created.
        """

        # create empty arrays
        centroids = np.zeros_like(old_centroids)
        cluster_k = centroids.shape[0]

        for i in range(0, cluster_k):
            sum_x = 0
            sum_y = 0
            amount = 0
            for j in range(0, cluster_mapping.shape[0]):
                if cluster_mapping[j] == i:
                    sum_x += data[j][0]
                    sum_y += data[j][1]
                    amount += 1

            # if no points assigned to centroid, take old coordinates
            if amount == 0:
                averaged_x = old_centroids[i][0]
                averaged_y = old_centroids[i][1]
            else:
                averaged_x = sum_x / amount
                averaged_y = sum_y / amount

            norm = sqrt(pow(averaged_x, 2) + pow(averaged_y, 2))
            centroids[i][0] = averaged_x / norm
            centroids[i][1] = averaged_y / norm

        return centroids
