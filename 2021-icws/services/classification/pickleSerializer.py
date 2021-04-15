import pickle


class PickleSerializer:
    """
    A class for serializing python objects.
    [Warning: The pickle module is not secure. Only unpickle data you trust.]
    see https://docs.python.org/3/library/pickle.html
    """

    @staticmethod
    def serialize(obj, file_path):
        """
        Serializes the given python object and stores it
        at the given location.
        """
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def deserialize(file_path):
        """
        Deserializes the file behind the given url
        to a python object.
        """
        with open(file_path, 'rb') as file:
            return pickle.load(file)
