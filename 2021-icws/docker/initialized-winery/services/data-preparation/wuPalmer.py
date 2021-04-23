import numpy as np
import math
import networkx as nx
from taxonomyLoadingService import TaxonomyLoadingService


class WuPalmerService:
    """
    A service wrapping the data preparation functionality using the Wu-Palmer similarity measure
    """

    @classmethod
    async def wu_palmer_data_preparation(cls, entities, output_file_path, attributes):

        print('Executing Wu-Palmer data preparation...')
        try:

            # perform comparison
            result = cls.calculate_pairwise_distance(entities, attributes)

            # serialize result
            np.savetxt(output_file_path, result)

        except Exception as ex:
            file = open(output_file_path, 'w')
            file.write(str(ex))
            file.close()

    @classmethod
    def calculate_pairwise_distance(cls, entities, attributes):
        """
        Calculates the pairwise distance and returns the distance matrix.
        """

        result = np.empty((len(entities), len(entities)))
        print('Starting pairwise distance calculation...')
        for i in range(0, result.shape[0]):
            for j in range(0, result.shape[0]):
                result[i][j] = cls.calculate_distance(entities[i], entities[j], attributes)
        print('Finished pairwise distance calculation. Returning distance matrix!')
        return result

    @classmethod
    def calculate_distance(cls, entity_1, entity_2, attributes):
        """
        Calculate the distance between two entities
        """

        print('Calculating distance between entity \'' + str(entity_1) + '\' and entity \'' + str(entity_2) + '\'!')
        return cls.transform_square_inverse(cls.calculate_similarity(entity_1, entity_2, attributes))

    @classmethod
    def transform_square_inverse(cls, similarity):
        """
        Returns the (1/sqrt(2)) * sqrt(s(i,i) + s(j,j) - 2s(i,j)) = sqrt(2) * sqrt(2 (1 - s))
        as distance with s being the similarity and 1 as the maxSimilarity.
        Due to the factor sqrt(2) the distance is between 0 and 1.
        """
        max_similarity = 1.0
        return (1.0 / math.sqrt(2.0)) * math.sqrt(2 * max_similarity - 2 * similarity)

    @classmethod
    def calculate_similarity(cls, entity_1, entity_2, attributes):
        """
        Returns the similarity between the two given entities
        """

        aggregation_values = []

        # iterate all attributes that are available for both entities and that are defined in the given list
        for attribute in attributes:
            if attribute not in entity_1.attributes or attribute not in entity_2.attributes:
                continue

            entity_1_attribute_values = entity_1.attributes[attribute].split(',')
            entity_2_attribute_values = entity_2.attributes[attribute].split(',')
            if len(entity_1_attribute_values) == 0 or len(entity_2_attribute_values) == 0:
                continue

            print('Attribute \'' + attribute + '\' available for both entities.')

            # compare attribute values and append for aggregation
            aggregation_values.append(cls.compare_attributes_symmaxmean(attribute, entity_1_attribute_values, entity_2_attribute_values))

        print('Retrieved ' + str(len(aggregation_values)) + ' to aggregate!')
        return cls.aggregate_mean(aggregation_values)

    @classmethod
    def aggregate_mean(cls, aggregation_values):
        """
        Aggregates the given values by using the mean
        """

        result = 0.0
        for value in aggregation_values:
            result += value
        return result / len(aggregation_values)

    @classmethod
    def compare_attributes_symmaxmean(cls, attribute, values_1, values_2):
        """
        Compares two attributes with symmetrical observation, maximum element selection, and averaging.
        """

        sum1 = 0.0
        sum2 = 0.0

        # Sum over a in first
        for a in values_1:
            # Get maximum compare_wu_palmer(a, b) with b in second
            max_value = 0.0
            for b in values_2:
                temp = cls.compare_wu_palmer(attribute, a, b)
                if temp > max_value:
                    max_value = temp

            sum1 += max_value

        # Normalize to size of first
        sum1 /= len(values_1)

        # Sum over b in second
        for b in values_2:
            # Get maximum compare_wu_palmer(b, a) with a in first
            max_value = 0.0
            for a in values_1:
                temp = cls.compare_wu_palmer(attribute, b, a)
                if temp > max_value:
                    max_value = temp

            sum2 += max_value

        # Normalize to size of second
        sum2 /= len(values_2)

        # Combine both sums
        return 0.5 * (sum1 + sum2)

    @classmethod
    def compare_wu_palmer(cls, attribute, value_1, value_2):
        print('Comparing values for attribute \'' + attribute + '\': ' + value_1 + "; " + value_2)

        # load taxonomy related to attribute
        taxonomy = TaxonomyLoadingService.load(attribute)

        # Get directed graph
        d_graph = taxonomy.graph

        # Get undirected graph
        ud_graph = d_graph.to_undirected()

        # Get lowest reachable node from both
        lowest_common_ancestor = nx.algorithms.lowest_common_ancestors.lowest_common_ancestor(d_graph, value_1, value_2)

        # Get root of graph
        root = [n for n, d in d_graph.in_degree() if d == 0][0]

        # Count edges - weight is 1 per default
        d1 = nx.algorithms.shortest_paths.generic.shortest_path_length(ud_graph, value_1, lowest_common_ancestor)
        d2 = nx.algorithms.shortest_paths.generic.shortest_path_length(ud_graph, value_2, lowest_common_ancestor)
        d3 = nx.algorithms.shortest_paths.generic.shortest_path_length(ud_graph, lowest_common_ancestor, root)

        # if first and second, both is the root
        if d1 + d2 + 2 * d3 == 0.0:
            return 0.0

        return 2 * d3 / (d1 + d2 + 2 * d3)
