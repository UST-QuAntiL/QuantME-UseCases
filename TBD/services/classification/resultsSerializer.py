import ast
import codecs
import numpy as np
from qiskit.result import Result
from qiskit.qobj.utils import MeasLevel

class ResultsSerializer:
    """
    A class for serializing qiskit.result.Result objects or lists thereof
    """

    @staticmethod
    def serialize(results, file_path):
        """
        Serializes the given list of results
        """

        if (type(results) != list):
            results = [results]

        with codecs.open(file_path, 'a', 'utf-8') as file:
            for i in range(len(results)):
                result = results[i].to_dict()

                for j in range(len(result['results'])):
                    # convert enum type to int
                    result['results'][j]['meas_level'] = int(result['results'][j]['meas_level'])

                    # convert statevector array to string
                    data = result['results'][j]['data']
                    if 'statevector' in data.keys():
                        statev_str = np.array2string(data['statevector'], separator=',', max_line_width=float('inf'))
                        result['results'][j]['data']['statevector'] = statev_str

                result_string = str(result)
                result_string = result_string.replace('\n', '')
                file.write(result_string)
                if i != len(results) - 1:
                    file.write('\n')

    @staticmethod
    def deserialize(file_path):
        """
        Deserializes the file behind the given url
        to list of results
        """
        results = []

        with codecs.open(file_path, 'r', 'utf-8') as file:
            for line in file:
                result = ast.literal_eval(line)

                for i in range(len(result['results'])):
                    # convert int back to enum type
                    result['results'][i]['meas_level'] = MeasLevel(result['results'][i]['meas_level'])

                    # convert statevector array back to np.array type
                    data = result['results'][i]['data']
                    if 'statevector' in data.keys():
                        statev = data['statevector']
                        statev = ast.literal_eval(statev)
                        statev = np.array(statev)
                        result['results'][i]['data']['statevector'] = statev

                results.append(Result.from_dict(result))

        return results
