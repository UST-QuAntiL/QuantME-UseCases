"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""
import json

from taxonomy import Taxonomy
from networkx.readwrite import json_graph

# we store the mapping between attribute names
# and their taxonomy names with the format
# [attribute_name, taxonomy_name]
attribute_taxonomy_mapping = {
    'DominanteFarbe': 'Farbe',
    'DominanterZustand': 'Zustand',
    'DominanteCharaktereigenschaft': 'Typus',
    'DominanterAlterseindruck': 'Alterseindruck'
}


class TaxonomyLoadingService:
    """
    A service class loading taxonomies for the muse repository.
    Moreover, this service encapsulates the logic which attribute
    is mapped to which taxonomy.
    """

    @classmethod
    def load_from_json(cls, name):
        """
        Loads a taxonomy object from the given json file and name.
        """

        name_with_extension = str(name) + ".json"
        file_name = "taxonomies/" + name_with_extension

        with open(file_name) as file_object:
            graph_json = json.load(file_object)

        graph = json_graph.node_link_graph(graph_json)
        return Taxonomy(graph)

    @classmethod
    def load(cls, attribute):
        """
        Loads the taxonomy that correspond to the given attribute name.
        """

        return cls.load_from_json(attribute_taxonomy_mapping[str(attribute)])
