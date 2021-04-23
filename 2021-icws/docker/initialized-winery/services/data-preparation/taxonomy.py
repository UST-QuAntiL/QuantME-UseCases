"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""


class Taxonomy:
    """
    A class representing a taxonomy from the muse repository.
    """

    def __init__(self, graph):
        self.__graph = graph

    @property
    def name(self):
        return str(self.get_root())

    @property
    def graph(self):
        return self.__graph

    def contains(self, element):
        """
        Check if element is in the taxonomy graph.
        """
        return self.graph.has_node(element)

    def get_root(self):
        """
        Returns the root of the taxonomy, i.e. of graph (tree).
        """
        return [n for n,d in self.graph.in_degree() if d == 0][0]
