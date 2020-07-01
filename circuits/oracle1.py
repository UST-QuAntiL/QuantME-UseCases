from qiskit.aqua.components.oracles import TruthTableOracle

oracle = TruthTableOracle(['1111', '0101'], optimization=False, mct_mode='basic')
oracle.construct_circuit()

def get_circuit(**kwargs):
    """Get oracle circuit."""
    return oracle.circuit