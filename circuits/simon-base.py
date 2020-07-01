from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit

qc = QuantumCircuit()

q = QuantumRegister(4, 'q')
c = ClassicalRegister(2, 'c')

qc.add_register(q)
qc.add_register(c)

# TODO

def get_circuit(**kwargs):
    """Get base circuit of Simon's algorithm."""
    return qc
