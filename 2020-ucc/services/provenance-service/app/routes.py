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

from app import app, unfolding_utils
from flask import jsonify, abort, request


@app.route('/provenance-service', methods=['POST'])
def mitigate_error():
    """Mitigate the readout-error from the given result distribution."""

    app.logger.info('Received Post request to mitigate error...')
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

    if 'QPU' not in request.json:
        app.logger.error("QPU not defined in request")
        abort(400, "QPU not defined in request")
    qpu = request.json['QPU']

    if 'UnfoldingTechnique' not in request.json:
        app.logger.error("UnfoldingTechnique not defined in request")
        abort(400, "UnfoldingTechnique defined in request")
    unfolding_technique = request.json['UnfoldingTechnique']
    if not unfolding_technique == 'Correction Matrix':
        app.logger.error("UnfoldingTechnique is not supported. Currently only Correction Matrix can be used")
        abort(400, "UnfoldingTechnique is not supported. Currently only Correction Matrix can be used")

    max_age = request.json['MaxAge']

    access_token = request.json['AccessToken']

    if 'Result' not in request.json:
        app.logger.error("Result not defined in request")
        abort(400, "Result not defined in request")
    result = request.json['Result']
    app.logger.info("Result to mitigate: " + result)

    app.logger.info("Passed input is valid")

    t = threading.Thread(target=unfolding_utils.mitigate_error, args=(correlation_Id, return_address, qpu, max_age, result, access_token))
    t.daemon = True
    t.start()

    return jsonify({'Status': "Circuit execution process initiated"}), 200
