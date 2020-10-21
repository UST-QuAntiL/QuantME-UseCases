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
import threading

from app import app, oracle_replacer
from flask import jsonify, abort, request


@app.route('/oracle-service', methods=['POST'])
def expand_oracle():
    """Expand one or multiple oracles in the given quantum circuit with the given oracle code."""

    app.logger.info('Received Post request to expand oracles...')
    if not request.json:
        app.logger.error("Service currently only supports JSON")
        abort(400, "Only Json supported")

    if 'CorrelationId' not in request.json:
        app.logger.error("CorrelationId not defined in request")
        abort(400, "CorrelationId not defined in request")
    correlation_Id = request.json['CorrelationId']
    app.logger.info("CorrelationId: " + correlation_Id)

    if 'ReturnAddress' not in request.json:
        app.logger.error("ReturnAddress not defined in request")
        abort(400, "ReturnAddress not defined in request")
    return_address = request.json['ReturnAddress']
    app.logger.info("ReturnAddress: " + return_address)

    if 'CircuitId' not in request.json:
        app.logger.error("CircuitId not defined in request")
        abort(400, "CircuitId not defined in request")

    if 'OracleId' not in request.json:
        app.logger.error("OracleId not defined in request")
        abort(400, "OracleId not defined in request")

    circuit_Id = request.json['CircuitId']
    oracle_Id = request.json['OracleId']
    app.logger.info("Extending oracles with Ids '" + str(oracle_Id) + "' on circuit with Id " + str(circuit_Id))

    if 'ProgrammingLanguage' not in request.json:
        app.logger.error("ProgrammingLanguage not defined in request")
        abort(400, "ProgrammingLanguage not defined in request")

    programming_language = str(request.json['ProgrammingLanguage'])
    app.logger.info('ProgrammingLanguage: ' + programming_language)
    if not programming_language == 'Qiskit':
        app.logger.error("ProgrammingLanguage is not supported. Currently only Qiskit can be used")
        abort(400, "ProgrammingLanguage is not supported. Currently only Qiskit can be used")

    if 'OracleCircuitUrl' not in request.json:
        app.logger.error("OracleCircuitUrl not defined in request")
        abort(400, "OracleCircuitUrl not defined in request")
    oracle_url = request.json['OracleCircuitUrl']

    if 'QuantumCircuit' not in request.json:
        app.logger.error("QuantumCircuit not defined in request")
        abort(400, "QuantumCircuit not defined in request")

    app.logger.info("Passed input is valid")

    t = threading.Thread(target=oracle_replacer.replace_oracles, args=(circuit_Id, oracle_Id, oracle_url, correlation_Id, return_address, request.json['QuantumCircuit'].encode('utf-8')))
    t.daemon = True
    t.start()

    return jsonify({'Status': "Oracle expansion process initiated"}), 200
