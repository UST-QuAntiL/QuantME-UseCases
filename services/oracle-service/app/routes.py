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

from app import app
from flask import jsonify, abort, request
from qiskit import transpile
from qiskit.transpiler.exceptions import TranspilerError
import logging
import json
import base64
import tempfile
import os
import shutil
import sys
import importlib

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

    if not 'QuantumCircuit' in request.json:
        app.logger.error("QuantumCircuit not defined in request")
        abort(400, "QuantumCircuit not defined in request")

    app.logger.info("Passed input is valid")

    # write quantum circuit qiskit file to temp directory
    quantum_circuit_bytes = base64.decodebytes(request.json['QuantumCircuit'].encode('utf-8'))
    temp_dir = tempfile.mkdtemp()
    file_name = "circuit_code_" + str(circuit_Id)
    with open(os.path.join(temp_dir, file_name + ".py"), "wb") as f:
        f.write(quantum_circuit_bytes)
    sys.path.append(temp_dir)

    app.logger.info("Created file at " + os.path.join(temp_dir, file_name + ".py"))

    # get circuit as code
    mod = importlib.import_module(file_name)
    circuit_code = mod.get_circuit()

    # extract classical and quantum register for manipulations
    if len(circuit_code.qubits) == 0:
        app.logger.error("QuantumCircuit uses no qubits. Aborting...")
        abort(400, "QuantumCircuit uses no qubits.")
    if len(circuit_code.clbits) == 0:
        app.logger.error("QuantumCircuit uses no classical bits. Aborting...")
        abort(400, "QuantumCircuit uses no classical bits.")
    quantum_register = circuit_code.qubits[0].register
    classical_register = circuit_code.clbits[0].register
    app.logger.info("QuantumCircuit contains classical register with " + str(classical_register.size) + " bits and quantum register with " + str(quantum_register.size) + " qubits.")

    # TODO: load oracle; manipulate quantum circuit

    sys.path.remove(temp_dir)
    shutil.rmtree(temp_dir, ignore_errors=True)

    return jsonify({'Test': "Test123"}), 200
