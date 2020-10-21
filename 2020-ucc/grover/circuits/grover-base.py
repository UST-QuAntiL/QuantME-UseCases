from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit


# create the diffuser gate (c.f. https://qiskit.org/textbook/ch-algorithms/grover.html)
def diffuser(nqubits):
    qc = QuantumCircuit(nqubits)
    # Apply transformation |s> -> |00..0> (H-gates)
    for qubit in range(nqubits):
        qc.h(qubit)
    # Apply transformation |00..0> -> |11..1> (X-gates)
    for qubit in range(nqubits):
        qc.x(qubit)
    # Do multi-controlled-Z gate
    qc.h(nqubits - 1)
    qc.mct(list(range(nqubits - 1)), nqubits - 1)  # multi-controlled-toffoli
    qc.h(nqubits - 1)
    # Apply transformation |11..1> -> |00..0>
    for qubit in range(nqubits):
        qc.x(qubit)
    # Apply transformation |00..0> -> |s>
    for qubit in range(nqubits):
        qc.h(qubit)
    # We will return the diffuser as a gate
    U_s = qc.to_gate()
    U_s.name = "$Diff$"
    return U_s


n = 5
qc = QuantumCircuit()

q = QuantumRegister(n, 'q')
c = ClassicalRegister(n, 'c')

qc.add_register(q)
qc.add_register(c)

# create initial superposition
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])
qc.h(q[4])

# start Grover iterations (4 required for 5 qubits)
####### iteration 1 #######
qc.barrier()
# area to insert oracle
qc.barrier()
qc.append(diffuser(n), [0, 1, 2, 3, 4])

####### iteration 2 #######
qc.barrier()
# area to insert oracle
qc.barrier()
qc.append(diffuser(n), [0, 1, 2, 3, 4])

####### iteration 3 #######
qc.barrier()
# area to insert oracle
qc.barrier()
qc.append(diffuser(n), [0, 1, 2, 3, 4])

####### iteration 4 #######
qc.barrier()
# area to insert oracle
qc.barrier()
qc.append(diffuser(n), [0, 1, 2, 3, 4])

qc.barrier()

qc.measure([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])


def get_circuit(**kwargs):
    """Get base circuit of Grover's algorithm for 5 qubits which performs 4 Grover iterations."""
    return qc
