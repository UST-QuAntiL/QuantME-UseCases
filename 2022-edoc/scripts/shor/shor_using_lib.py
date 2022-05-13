import math
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor

N = 15
backend = Aer.get_backend('aer_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)
shor = Shor(quantum_instance=quantum_instance)
result = shor.factor(N)
circuit = shor.construct_circuit(N)
print(circuit)
print(f"The list of factors of {N} as computed by the Shor's algorithm is {result.factors[0]}.")

print(f'Computed of qubits for circuit: {4 * math.ceil(math.log(N, 2)) + 2}')
print(f'Actual number of qubits of circuit: {shor.construct_circuit(N).num_qubits}')
