from qiskit import QuantumRegister, QuantumCircuit

qc = QuantumCircuit()
q = QuantumRegister(5, 'q')
qc.add_register(q)

# searched bit string: s = 11011
qc.x(q[2])
qc.h(q[4])
qc.mct(list(range(4)), 4)
qc.h(q[4])
qc.x(q[2])

def get_circuit(**kwargs):
    """Get oracle circuit."""
    return qc