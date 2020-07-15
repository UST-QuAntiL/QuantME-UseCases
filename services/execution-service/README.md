# Execution-Service

Service to execute a given quantum circuit on a defined quantum computer.

## Setup

Install packages as listed in [requirements.txt](requirements.txt). 
Python 3.7 is required.

Execute the following command:

```
python -m flask run --host=0.0.0.0 --port=8082
```

The execution service is accessible on [localhost:8082/execution-service](http://localhost:8082/execution-service).

## Circuit Execution Request

Send CorrelationId, ReturnAddress, ProgrammingLanguage, Provider, QPU, AccessToken, QuantumCircuit, and Shots to the API to execute the given circuit on the specified QPU with the defined number of shots and to receive the result after the execution at the specified address via POST.

`POST /execution-service/`  
```
{  
    "CorrelationId": "Unique Id that is returned in the response to correlate it with the request",
    "ReturnAddress": "The address to send the execution result to",
    "ProgrammingLanguage": "Programming language of the circuit and oracle (only qiskit supported at the moment)",
    "Provider": "The name of the quantum cloud offering to use",
    "QPU": "The name of the QPU for the execution",
    "AccessToken": "The access token to access the selected QPU for execution",
    "QuantumCircuit": "Quantum circuit to execute",
    "Shots": "Number of runs that should be performed (default: 1024)"
}  
```

## Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss

Dies ist ein Forschungsprototyp.
Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
