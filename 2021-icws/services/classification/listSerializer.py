import codecs
import ast

class ListSerializer:
    """
    A class for serializing Python lists and dictionaries (or lists of dictionaries or vice versa)
    NOTE:   This requires that list/dict can be parsed back from the
            string it produces, which is usually the case if only builtin
            data types are used.
    """

    @staticmethod
    def serialize(list_or_dictionary, file_path):
        """
        Serializes the given list or dictionary
        """

        with codecs.open(file_path, 'a', 'utf-8') as file:
                file.write(str(list_or_dictionary))

    @staticmethod
    def deserialize(file_path):
        """
        Deserializes the file behind the given url
        to list or dict
        """

        with codecs.open(file_path, 'r', 'utf-8') as file:
            list_string = file.read()
            return ast.literal_eval(list_string)
