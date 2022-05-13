from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram

# Modular Exponentiation Function
# convert factoring problem to period finding problem
# divide number N into a guessed number a and compute the remainder
# --> for good guesses of a, this function is periodic as we increase the power of a
def c_amod15(a,power):
	U = QuantumCircuit(4)
	for iteration in range(power):
		U.swap(2,3)
		U.swap(1,2)
		U.swap(0,1)
		for q in range(4):
			U.x(q)
		U = U.to_gate()
		U.name = "%i^%i mod 15" %(a, power)
		c_U = U.control()
		return c_U


# Quantum Fourier Transform
# Find period, this is where the speedup comes from
def qft_dagger(n):
	qc = QuantumCircuit(n)
	for qubit in range(n//2):
		qc.swap(qubit, n-qubit-1)
	for j in range(n):
		for m in range(j):
			qc.cp(-np.pi/float(2**(j-m)), m, j)
		qc.h(j)
	qc.name = "QFT dagger"
	return qc


if __name__ == '__main__':
	n_count = 8
	a = 7

	qc = QuantumCircuit(n_count+4, n_count)

	for q in range(n_count):
		qc.h(q)

	qc.x(3+n_count)

	for q in range(n_count):
		qc.append(c_amod15(a, 2**q), [q]+[i+n_count for i in range(4)])

	qc.append(qft_dagger(n_count), range(n_count))

	qc.measure(range(n_count), range(n_count))

	print(qc)

	backend = Aer.get_backend('qasm_simulator')
	results = execute(qc, backend, shots=1024).result()
	counts_result = results.get_counts()
	print(results)
	print(counts_result)

# TODO
# Use period Compute Factors of Original Number
# a = guessed number
# r = period of Modular Exponention Function
# p = a^(r/2)-1
# q = a^(r*sqrt(2))+1
# N = number to factor
# p and q are not necessarily the factors of N. But with high probability
# they will have cofactors with N which we can compute efficiently. If our
# magic number aren't integers, we can just use another guess for a.





