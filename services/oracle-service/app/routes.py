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

@app.route('/oracle-service', methods=['POST'])
def expand_oracle():
    """Expand an oracle in the given quantum circuit with the given oracle code."""

    app.logger.info('Received Post request to expand oracle: ' + request.json)

    if not request.json:
        app.logger.error("Service currently only supports JSON")
        abort(400)

    if not 'ProgrammingLanguage' in request.json:
        app.logger.error("ProgrammingLanguage not defined in request")
        abort(400)

    if not 'OracleId' in request.json:
        app.logger.error("OracleId not defined in request")
        abort(400)

    if not 'OracleCircuitUrl' in request.json:
        app.logger.error("OracleCircuitUrl not defined in request")
        abort(400)

    if not 'QuantumCircuit' in request.json:
        app.logger.error("QuantumCircuit not defined in request")
        abort(400)

    app.logger.info("Passed input is valid")
    app.logger.info(request.json)

    return jsonify({'Test': "Test123"}), 200
