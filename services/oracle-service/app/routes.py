# ******************************************************************************
#  Copyright (c) 2020 University of Stuttgart
#
#  See the NOTICE file(s) distributed with this work for additional
#  information regarding copyright ownership.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ******************************************************************************
import copy

from qiskit.circuit import Qubit
from qiskit.converters import circuit_to_dag, dag_to_circuit

from app import app, qiskit_importer
from flask import jsonify, abort, request


@app.route('/oracle-service', methods=['POST'])
def expand_oracle():
    """Expand an oracle in the given quantum circuit with the given oracle code."""

    app.logger.info('Received Post request to expand oracle...')
    if not request.json:
        app.logger.error("Service currently only supports JSON")
        abort(400, "Only Json supported")

    if not 'CircuitId' in request.json:
        app.logger.error("CircuitId not defined in request")
        abort(400, "CircuitId not defined in request")

    if not 'OracleId' in request.json:
        app.logger.error("OracleId not defined in request")
        abort(400, "OracleId not defined in request")

    circuit_Id = request.json['CircuitId']
    oracle_Id = request.json['OracleId']
    app.logger.info("Extending oracle with Id " + str(oracle_Id) + " on circuit with Id " + str(circuit_Id))

    if not 'ProgrammingLanguage' in request.json:
        app.logger.error("ProgrammingLanguage not defined in request")
        abort(400, "ProgrammingLanguage not defined in request")

    programming_language = str(request.json['ProgrammingLanguage'])
    app.logger.info('ProgrammingLanguage: ' + programming_language)
    if not programming_language == 'Qiskit':
        app.logger.error("ProgrammingLanguage is not supported. Currently only Qiskit can be used")
        abort(400, "ProgrammingLanguage is not supported. Currently only Qiskit can be used")

    if not 'OracleCircuitUrl' in request.json:
        app.logger.error("OracleCircuitUrl not defined in request")
        abort(400, "OracleCircuitUrl not defined in request")
    oracle_url = request.json['OracleCircuitUrl']

    if not 'QuantumCircuit' in request.json:
        app.logger.error("QuantumCircuit not defined in request")
        abort(400, "QuantumCircuit not defined in request")

    app.logger.info("Passed input is valid")

    # get circuit as qiskit object and check for validity
    circuit_code = qiskit_importer.get_circuit_from_binary(circuit_Id, request.json['QuantumCircuit'].encode('utf-8'))
    if len(circuit_code.qubits) == 0:
        app.logger.error("QuantumCircuit uses no qubits. Aborting...")
        abort(400, "QuantumCircuit uses no qubits.")
    if len(circuit_code.clbits) == 0:
        app.logger.error("QuantumCircuit uses no classical bits. Aborting...")
        abort(400, "QuantumCircuit uses no classical bits.")
    app.logger.info("QuantumCircuit contains " + str(len(circuit_code.clbits)) + " classical bits and " + str(
        len(circuit_code.qubits)) + " qubits.")

    # get oracle circuit as code
    oracle_code = qiskit_importer.get_oracle_from_url(oracle_url, oracle_Id)
    if oracle_code is None:
        abort(400, "Error while importing oracle code from given url!")
    app.logger.info("OracleCircuit contains " + str(len(oracle_code.qubits)) + " qubits.")

    # circuit and oracle should operate on the same set of qubits
    if len(oracle_code.qubits) != len(circuit_code.qubits):
        app.logger.error("Oracle has to operate on the same size of quantum register than the quantum circuit!")
        abort(400, "Oracle has to operate on the same size of quantum register than the quantum circuit!")

    # transform circuit and oracle to dag format to enable easier modifications
    dag_circuit = circuit_to_dag(circuit_code)
    dag_oracle = circuit_to_dag(oracle_code)
    dag_circuit_back = copy.deepcopy(dag_circuit)

    # insert the oracle into the circuit at the specified position
    removed_operations = []
    for node in dag_circuit.topological_nodes():
        if node.type == 'in' and isinstance(node.wire, Qubit):
            # find operation node for depth defined by 'oracle_Id'
            i = 0
            node_to_append_oracle = None
            for node_on_wire in dag_circuit.nodes_on_wire(node.wire, only_ops=True):
                i += 1
                if i == oracle_Id:
                    # this is the last operation that should be performed before the oracle is inserted
                    node_to_append_oracle = node_on_wire
                    break
            if node_to_append_oracle is None:
                app.logger.error("Unable to insert oracle at defined position!")
                abort(400, "Unable to insert oracle at defined position!")

            # remove descendant operations of the node temporarily from the dag
            app.logger.info("Inserting oracle on wire " + str(node.wire) + " after operation with name "
                            + node_to_append_oracle.name)
            removed_operations.append(dag_circuit.descendants(node_to_append_oracle))
            for descendant in dag_circuit.descendants(node_to_append_oracle):
                if descendant.type == 'op':
                    dag_circuit.remove_op_node(descendant)

            # remove ancestor operations in the backup dag to store the circuit part behind the oracle
            for ancestors in dag_circuit_back.ancestors(node_to_append_oracle):
                if ancestors.type == 'op':
                    dag_circuit_back.remove_op_node(ancestors)
            dag_circuit_back.remove_op_node(node_to_append_oracle)

    # compose front part of circuit, oracle, and back part of circuit to overall circuit
    dag_circuit.compose(dag_oracle)
    dag_circuit.compose(dag_circuit_back)

    # TODO: return circuit
    final_circuit = dag_to_circuit(dag_circuit)
    final_circuit.draw(output='mpl', filename='circuit.png')

    return jsonify({'Test': "Test123"}), 200
