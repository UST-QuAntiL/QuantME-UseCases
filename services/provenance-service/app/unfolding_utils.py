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
import time
import requests

from app import app


def mitigate_error(correlation_Id, return_address, qpu, max_age, result):
    """Mitigate the readout-error in the given result distribution"""

    # TODO
    mitigated_result = result

    time.sleep(5)
    camunda_callback = requests.post(return_address, json={"messageName": correlation_Id, "processVariables": {
        "executionResult": {"value": str(mitigated_result), "type": "String"}}})
    app.logger.info("Callback returned status code: " + str(camunda_callback.status_code))
