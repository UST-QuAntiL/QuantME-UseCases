# Oracle-Service

Service to replace an oracle in a given quantum circuit by a given subcircuit.

## Setup

Install packages as listed in [requirements.txt](requirements.txt). 
Python 3.7 is required.

Execute the following command:

```
python -m flask run --host=0.0.0.0 --port=8081
```

The oracle service is accessible on [localhost:8081/oracle-service](http://localhost:8081/oracle-service).

## Oracle Replacement Request

Send CorrelationId, ReturnAddress, CircuitId, OracleId, ProgrammingLanguage, OracleCircuitUrl, and the QuantumCircuit to the API to get the resulting circuit with the expanded oracle at the specified address via POST.

`POST /oracle-service/`  
```
{  
    "CorrelationId": "Unique Id that is returned in the response to correlate it with the request",
    "ReturnAddress": "The address to send the resulting circuit to",
    "CircuitId": "Id of the quantum circuit to identify it uniquely",
    "OracleId": "List of depths in the circuit where the oracle circuit should be inserted (comma separated if multiple Ids are used)",
    "ProgrammingLanguage": "Programming language of the circuit and oracle (only qiskit supported at the moment)",
    "OracleCircuitUrl": "Url where the oracle circuit is located",
    "QuantumCircuit": "Base64 encoded python file with circuit"
}  
```

## Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss

Dies ist ein Forschungsprototyp.
Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
