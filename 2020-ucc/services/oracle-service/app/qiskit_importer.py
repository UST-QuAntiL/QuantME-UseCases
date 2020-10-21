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
import base64
import importlib
import os
import shutil
import sys
import tempfile
from urllib import request as urllib_request

from app import app


def get_oracle_from_url(oracle_url):
    """Download an oracle from the given URL and provide it as Qiskit object"""

    # get oracle circuit from URL
    app.logger.info("Downloading oracle circuit from URL: " + oracle_url)
    temp_dir = tempfile.mkdtemp()
    oracle_file_name = "oracle_code";
    with open(os.path.join(temp_dir, oracle_file_name + ".py"), "w") as f:
        f.write(urllib_request.urlopen(oracle_url).read().decode("utf-8"))
    sys.path.append(temp_dir)
    app.logger.info("Created file at " + os.path.join(temp_dir, oracle_file_name + ".py"))

    # get oracle circuit as code
    try:
        oracle_mod = importlib.import_module(oracle_file_name)
        importlib.reload(oracle_mod)

        circuit = oracle_mod.get_circuit()

        sys.path.remove(temp_dir)
        shutil.rmtree(temp_dir, ignore_errors=True)
        return circuit
    except:
        app.logger.error("Error while importing oracle code from given url!")
        return None


def get_circuit_from_binary(circuit_base64):
    """Convert the given bas64 encoded python file to an qiskit oracle object"""

    # write quantum circuit qiskit file to temp directory
    quantum_circuit_bytes = base64.decodebytes(circuit_base64)
    temp_dir = tempfile.mkdtemp()
    with open(os.path.join(temp_dir, "circuit_code_file.py"), "wb") as f:
        f.write(quantum_circuit_bytes)
    sys.path.append(temp_dir)
    app.logger.info("Created file at " + os.path.join(temp_dir, "circuit_code_file.py"))

    # get quantum circuit as code
    try:
        import circuit_code_file
        importlib.reload(circuit_code_file)
        return circuit_code_file.get_circuit()
    finally:
        sys.path.remove(temp_dir)
        shutil.rmtree(temp_dir, ignore_errors=True)
