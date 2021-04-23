"""
Author: Daniel Fink
Email: daniel-fink@outlook.com
"""


class Entity:
    """
    Represents an entity for which machine learning techniques can be applied onto.
    """

    def __init__(self, uid):
        self.uid = uid

        # we store the attributes and the
        # associated values as dicts in the format
        # [attribute, [value1, value2, ...]]
        self.__attributes = dict()

    @property
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, value):
        self.__uid = value

    @property
    def attributes(self):
        return self.__attributes

    def __str__(self):
        """
        Returns the entity in a single string.
        """
        output = 'Entity[' + str(self.uid) + '] = '
        for attribute, value in self.attributes.items():
            output += str(attribute) + ": " + str(value) + ", "
        return output[:-2]
