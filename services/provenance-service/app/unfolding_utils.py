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
import ast
import time
import qiskit
import requests
from qiskit import IBMQ
from qiskit.ignis.mitigation.measurement import (complete_meas_cal, CompleteMeasFitter)
from qiskit.providers.jobstatus import JOB_FINAL_STATES
from datetime import datetime

from app import app

calibration_matrixes = {}


def mitigate_error(correlation_Id, return_address, qpu, max_age, result, access_token):
    """Mitigate the readout-error in the given result distribution"""
    app.logger.info('Result before mitigation: ' + result)
    meas_filter = get_correction_matrix(qpu, max_age, access_token, len(next(iter(ast.literal_eval(result)))))

    mitigated_results = result
    if meas_filter is not None:
        # Apply mitigation if matrix is successfully retrieved
        mitigated_results = meas_filter.apply(ast.literal_eval(result))
        app.logger.info('Result after mitigation: ' + str(mitigated_results))

    app.logger.info('Sending callback to ' + str(return_address))
    camunda_callback = requests.post(return_address, json={"messageName": correlation_Id, "processVariables": {
        "executionResult": {"value": str(mitigated_results), "type": "String"}}})
    app.logger.info("Callback returned status code: " + str(camunda_callback.status_code))


def get_correction_matrix(qpu, max_age, access_token, used_qubits):
    """Return a correction matrix for the given QPU whit the maximum age in minutes"""
    app.logger.info('Getting calibration matrix for QPU ' + qpu + ' with max age of ' + str(max_age) + ' minutes')

    # Check for existing calibration matrix
    existing_matrix = calibration_matrixes.get(qpu)
    if existing_matrix is not None:
        age = datetime.now() - existing_matrix['Date']
        app.logger.info('Calibration matrix for this QPU exists with age ' + str(age))
        if age.total_seconds() < max_age * 60:
            app.logger.info('Returning existing calibration matrix!')
            return existing_matrix['Calibration_Matrix']

    if access_token is None:
        app.logger.error('Unable to create new correction matrix without access key...')
        return None

    # Load account to enable execution of calibration circuits
    IBMQ.save_account(access_token, overwrite=True)
    IBMQ.load_account()

    provider = IBMQ.get_provider(group='open')
    backend = provider.get_backend(qpu)

    # Generate a calibration circuit for each state
    qr = qiskit.QuantumRegister(used_qubits)
    meas_calibs, state_labels = complete_meas_cal(qr=qr, circlabel='mcal')

    # Execute each calibration circuit and store results
    app.logger.info('Executing ' + str(len(meas_calibs)) + ' circuits to create calibration matrix...')
    cal_results = []
    for circuit in meas_calibs:
        app.logger.info('Executing circuit ' + circuit.name)
        cal_results.append(execute_job(circuit, backend))

    # Generate calibration matrix out of measurement results
    meas_fitter = CompleteMeasFitter(cal_results, state_labels, circlabel='mcal')
    app.logger.info('Calibration matrix:')
    app.logger.info(meas_fitter.cal_matrix)

    # Store calibration matrix for later reuse
    calibration_matrixes[qpu] = {"Date": datetime.now(), "Calibration_Matrix": meas_fitter.filter}
    return meas_fitter.filter


def execute_job(circuit, backend):
    """Execute a circuit on the specified backend"""
    job = qiskit.execute(circuit, backend=backend, shots=1000)

    job_status = job.status()
    while job_status not in JOB_FINAL_STATES:
        app.logger.info('The execution is still running')
        time.sleep(20)
        job_status = job.status()
    return job.result()
