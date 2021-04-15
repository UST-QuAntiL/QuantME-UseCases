import numpy as np
from qiskit.aqua.algorithms.classifiers.vqc import cost_estimate, return_probabilities
import math

class SPSAOptimizer():
    """
        Optimization (SPSA)
        adapted from qiskit.aqua.components.optimizers.SPSA
        https://qiskit.org/documentation/stubs/qiskit.aqua.components.optimizers.SPSA.html
    """

    @classmethod
    def initializeOptimization(cls, n_thetas, optimizer_params):
        # TODO: Calibrate optimizer parameters

        initial_thetas = np.random.default_rng().standard_normal(n_thetas)

        thetas_plus, thetas_minus, delta = generateDirections(0, initial_thetas, optimizer_params)
        return initial_thetas, thetas_plus, thetas_minus, delta

    @classmethod
    def optimize(cls, results, labels, thetas, delta, iteration, optimizer_params, is_statevector=False):
        """
            Parameters:
            - results: list of results to evaluate
                (results for theta, theta_plus, theta_minus in 3 equal portions and this exact order)
                OR (results for theta_plus, theta_minus in 2 equal portions in this exact order, see exact_costs parameter)
                The results are of type qiskit.result.Result
            - labels: array, the actual labels of the data (in correct order of course)
            - thetas: array, thetas used to generate these results (i.e. thetas of the current iteration
            - delta: array, analogous to thetas
            - iteration: int, current iteration
            - optimizer_params: array, parameters c0 through c4 for optimization (floats)
            - is_statevector: bool, states whether the results were computed on a statevector simulator or not
            - exact_costs: bool, this refers to the format of results. If True then results will
                be split into three portions, else into two (for theta_plus/theta_minus only)

            Returns: thetas, thetas_plus, thetas_minus, delta for next iteration (as arrays);
                costs_curr: float, the current costs. If compute_current_cost is True it will give
                the exact current costs, otherwise those for theta_minus which are close to the current costs
        """

        # this preprocessing ensures that the optimizer can work with both, a list of
        # results or a single qiskit.result.Result with multiple experiments
        n_results = len(results)
        results_list = True # determines whether results is a list of qiskit.result.Result or one single object of that type
        if (n_results == 1):
            results = results[0]
            n_results = len(results.results)
            results_list = False

        n_data = len(labels)
        n_classes = len(set(labels))
        exact_costs = n_results//n_data == 3 # determines whether results contain data for thetas/exact costs computation

        results_curr = results if exact_costs else None
        results_plus, results_minus = results, results
        indices_curr, indices_plus, indices_minus = None, None, None
        if (exact_costs and results_list):
            results_curr, results_plus, results_minus = np.array_split(results, 3)
        elif (results_list):
            results_plus, results_minus = np.array_split(results, 2)
        elif (exact_costs):
            indices_curr, indices_plus, indices_minus = np.array_split(range(3*n_data), 3)
        else:
            indices_plus, indices_minus = np.array_split(range(2*n_data), 2)

        probs_plus, pred_lbls_plus = cls.computeProbabilities(results_plus, is_statevector, n_data, n_classes, indices=indices_plus)
        probs_minus, pred_lbls_minus = cls.computeProbabilities(results_minus, is_statevector, n_data, n_classes, indices=indices_minus)
        costs_plus = cost_estimate(probs_plus, labels)
        costs_minus = cost_estimate(probs_minus, labels)

        costs_curr = None
        if (results_curr is not None):
            probs_curr, pred_lbls_curr = cls.computeProbabilities(results_curr, is_statevector, n_data, n_classes, indices=indices_curr)
            costs_curr = cost_estimate(probs_curr, labels)
        else:
            costs_curr = costs_minus

        g_spsa = (costs_plus - costs_minus) * delta / (2.0 * get_c_spsa(iteration, optimizer_params))
        # updated theta
        thetas = thetas - get_a_spsa(iteration, optimizer_params) * g_spsa

        thetas_plus, thetas_minus, delta = generateDirections(iteration, thetas, optimizer_params)

        return thetas, thetas_plus, thetas_minus, delta, costs_curr

    @classmethod
    def computeProbabilities(cls, results, is_statevector, n_data, n_classes, indices=None):
        """
            Compute probabilities from results
            results: either a list of qiskit.result.Result or one such object with multiple experiments
            indices: in the latter case: a list of the indices of the relevant experiments
        """
        circuit_id = 0
        predicted_probs = []
        predicted_labels = []
        counts = []
        for i in range(n_data):
            if is_statevector:
                if indices is not None:
                    temp = results.get_statevector(int(indices[i])) # cast to int, otherwise int32 will not be recognized as int
                else:
                    temp = results[i].get_statevector()
                outcome_vector = (temp * temp.conj()).real
                # convert outcome_vector to outcome_dict, where key
                # is a basis state and value is the count.
                # Note: the count can be scaled linearly, i.e.,
                # it does not have to be an integer.
                outcome_dict = {}
                bitstr_size = int(math.log2(len(outcome_vector)))
                for i, _ in enumerate(outcome_vector):
                    bitstr_i = format(i, '0' + str(bitstr_size) + 'b')
                    outcome_dict[bitstr_i] = outcome_vector[i]
            else:
                if indices is not None:
                    outcome_dict = results.get_counts(int(indices[i]))
                else:
                    outcome_dict = results[i].get_counts()

            counts.append(outcome_dict)
            circuit_id += 1

        probs = return_probabilities(counts, n_classes)
        predicted_probs.append(probs)
        predicted_labels.append(np.argmax(probs, axis=1))

        if len(predicted_probs) == 1:
            predicted_probs = predicted_probs[0]
        if len(predicted_labels) == 1:
            predicted_labels = predicted_labels[0]

        return predicted_probs, predicted_labels

def get_a_spsa(iteration, optimizer_params):
    c0, c1, c2, c3, c4 = optimizer_params
    return float(c0) / np.power(iteration + 1 + c4, c2)

def get_c_spsa(iteration, optimizer_params):
    c0, c1, c2, c3, c4 = optimizer_params
    return float(c1) / np.power(iteration + 1, c3)

def gen_delta(size):
    return 2 * np.random.default_rng().integers(2, size=size) - 1

def generateDirections(iteration, thetas, optimizer_params):
    c_spsa = get_c_spsa(iteration, optimizer_params)
    delta = gen_delta(size=thetas.shape[0])

    thetas_plus = thetas + c_spsa * delta
    thetas_minus = thetas - c_spsa * delta
    return thetas_plus, thetas_minus, delta