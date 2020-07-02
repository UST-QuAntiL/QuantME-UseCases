from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit

qc = QuantumCircuit()

q = QuantumRegister(4, 'q')
c = ClassicalRegister(4, 'c')

qc.add_register(q)
qc.add_register(c)

qc.h(q[0])
qc.h(q[1])

# we add an identity gate to enable adding the oracle at depth one on all qubits as qiskit does not allow an explicit placeholder
qc.id(q[2])
qc.id(q[3])
qc.id(q[2])
qc.id(q[3])

qc.h(q[0])
qc.h(q[1])

qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

def get_circuit(**kwargs):
    """Get base circuit of Simon's algorithm."""
    return qc
