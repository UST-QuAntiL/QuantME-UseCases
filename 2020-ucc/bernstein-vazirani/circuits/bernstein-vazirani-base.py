from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit

qc = QuantumCircuit()

q = QuantumRegister(5, 'q')
c = ClassicalRegister(5, 'c')

qc.add_register(q)
qc.add_register(c)

qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])

# add identity gates to the circuit to enable replacing the oracle after 2 gates per qubit
qc.i(q[0])
qc.i(q[1])
qc.i(q[2])
qc.i(q[3])

# ancilla qubit
qc.h(q[4])
qc.z(q[4])

qc.barrier()
# area to insert oracle
qc.barrier()

qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])

qc.i(q[4])

qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

def get_circuit(**kwargs):
    """Get base circuit of the Bernstein-Vazirani algorithm."""
    return qc