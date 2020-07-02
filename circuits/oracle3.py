from qiskit import QuantumRegister, QuantumCircuit

# Truth table:
# 00 | 10
# 01 | 10
# 10 | 01
# 11 | 01
# --> s=01

qc = QuantumCircuit()

q = QuantumRegister(4, 'q')

qc.add_register(q)

qc.x(q[2])
qc.cx(q[0], q[2])
qc.cx(q[0], q[3])

def get_circuit(**kwargs):
    """Get oracle circuit."""
    return qc