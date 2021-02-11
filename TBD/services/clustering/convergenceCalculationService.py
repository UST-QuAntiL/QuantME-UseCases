"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""

from math import sqrt, pow


class ConvergenceCalculationService:
    """
    A service class for all kind of convergence calculations.
    """

    @classmethod
    def calculate_averaged_euclidean_distance(cls, old_centroids, new_centroids):
        """
        Calculates the pairwise distance of the old and new centroid
        location, sum them up and divide by the amount of centroids.
        """

        result = 0.0
        for i in range(0, old_centroids.shape[0]):
            result += cls.calculate_euclidean_distance(old_centroids[i], new_centroids[i])
        return result / old_centroids.shape[0]

    @classmethod
    def calculate_euclidean_distance(cls, first, second):
        """
        Calculates the euclidean distance of the two vectors.
        """

        norm = 0.0
        for i in range(0, first.shape[0]):
            norm += pow(first[i] - second[i], 2)
        return sqrt(norm)
