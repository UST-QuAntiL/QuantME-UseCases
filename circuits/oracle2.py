from qiskit import QuantumRegister, QuantumCircuit

# Truth table:
# 00 | 00
# 01 | 01
# 10 | 10
# 11 | 11
# --> s=00

qc = QuantumCircuit()

q = QuantumRegister(4, 'q')

qc.add_register(q)

qc.cx(q[0], q[2])
qc.cx(q[1], q[3])

def get_circuit(**kwargs):
    """Get oracle circuit."""
    return qc