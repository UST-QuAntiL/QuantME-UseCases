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
import codecs
import copy
import pickle

import requests

from app import app, qiskit_importer
from qiskit.circuit import Qubit
from qiskit.converters import circuit_to_dag, dag_to_circuit


def replace_oracle_in_circuit(dag_circuit, dag_oracle, oracle_Id):
    dag_circuit_back = copy.deepcopy(dag_circuit)

    # insert the oracle into the circuit at the specified position
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
                return

            # remove descendant operations of the node temporarily from the dag
            app.logger.info("Inserting oracle on wire " + str(node.wire) + " after operation with name "
                            + node_to_append_oracle.name)
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
    return dag_circuit


def replace_oracles(circuit_Id, oracle_Id_string, oracle_url, correlation_Id, return_address, quantum_circuit):
    """Replace the oracles in the given circuit"""
    # get circuit as qiskit object and check for validity
    circuit_code = qiskit_importer.get_circuit_from_binary(quantum_circuit)
    if len(circuit_code.qubits) == 0:
        app.logger.error("QuantumCircuit uses no qubits. Aborting...")
        return
    if len(circuit_code.clbits) == 0:
        app.logger.error("QuantumCircuit uses no classical bits. Aborting...")
        return
    app.logger.info("QuantumCircuit contains " + str(len(circuit_code.clbits)) + " classical bits and " + str(
        len(circuit_code.qubits)) + " qubits.")

    # get oracle circuit as code
    oracle_code = qiskit_importer.get_oracle_from_url(oracle_url)
    if oracle_code is None:
        return
    app.logger.info("OracleCircuit contains " + str(len(oracle_code.qubits)) + " qubits.")

    # circuit and oracle should operate on the same set of qubits
    if len(oracle_code.qubits) != len(circuit_code.qubits):
        app.logger.error("Oracle has to operate on the same size of quantum register than the quantum circuit!")
        return

    # transform circuit and oracle to dag format to enable easier modifications
    dag_circuit = circuit_to_dag(circuit_code)
    dag_oracle = circuit_to_dag(oracle_code)

    # split Id string and replace the oracles on each position
    oracle_Ids = str(oracle_Id_string).split(",")
    app.logger.info("Replacing " + str(len(oracle_Ids)) + " oracles in the circuit with the given implementation!")
    for oracle_Id in reversed(oracle_Ids):  # we assume an order list of Ids here
        app.logger.info("Replacing oracle with Id: " + str(oracle_Id))
        dag_circuit = replace_oracle_in_circuit(dag_circuit, dag_oracle, int(oracle_Id))

    # build response to post to Camunda Rest API
    final_circuit = dag_to_circuit(dag_circuit)
    final_circuit_base64 = str(codecs.encode(pickle.dumps(final_circuit), "base64").decode())
    final_circuit_base64 = final_circuit_base64.encode('unicode_escape').decode("utf-8")  # double encode line break
    app.logger.info('Sending callback to ' + str(return_address))
    camunda_callback = requests.post(return_address, json={"messageName": correlation_Id, "processVariables":
        {"quantumCircuit": {"value": "{\"circuit\": \"" + final_circuit_base64 + "\"}", "type": "Json"}}})
    app.logger.info("Callback returned status code: " + str(camunda_callback.status_code))
