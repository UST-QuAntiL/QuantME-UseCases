from qiskit.circuit.library import ZFeatureMap, TwoLocal
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister

class VariationalSVMCircuitGenerator():

    @classmethod
    def generateCircuitTemplate(cls, nqbits, reps_featuremap, reps_varform, entanglement, measure=False):
        """
            Generates the quantum circuit for variational SVM, which
            consists of a FeatureMap and the variational form.
            Fixed FeatureMap to ZFeatureMap instance and variational form
            to RyRz (for simplicity)
        """
        # instanciate feature map and variational form
        feature_map = ZFeatureMap(nqbits, reps_featuremap)
        var_form = TwoLocal(nqbits, ['ry', 'rz'], "cz", entanglement, reps_varform)

        # create empty circuit
        qr = QuantumRegister(nqbits, name='q')
        cr = ClassicalRegister(nqbits, name='c')
        qc = QuantumCircuit(qr, cr)

        # append feature map and variational form
        qc.append(feature_map.to_instruction(), qr)
        qc.append(var_form.to_instruction(), qr)

        # add measurements
        if measure:
            qc.barrier(qr)
            qc.measure(qr, cr)

        return qc, feature_map.parameters, var_form.parameters

    @classmethod
    def generateCircuitParameterizations(cls, circuit, data: list, thetas: list):
        """
            Prepares the circuit parameterizations for the provided data points and thetas

                data: list of data points, shape N x d
                    where   N = number of data points
                            d = dimension of data
                theta: list of trainable parameters, shape n x d
                    with    n = number of parameterizations (with different set of thetas),
                            d = number of trainable parameters
        """
        n_parameterizations = len(data)
        n_dimensions = data.shape[1]
        fm_parameters, var_parameters = circuit[0][0].params, circuit[1][0].params
        fm_parameters, var_parameters = [param.name for param in fm_parameters], [param.name for param in var_parameters]

        parameterizations = []
        for theta in thetas:
            for datum in data:
                curr_params = dict(zip(fm_parameters, datum))
                curr_params.update(dict(zip(var_parameters, theta)))
                parameterizations.append(curr_params)

        return parameterizations