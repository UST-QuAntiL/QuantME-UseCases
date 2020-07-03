# Execution-Service

Service to execute a given quantum circuit on a defined quantum computer.

## Setup

Install packages as listed in [requirements.txt](requirements.txt). 
Python 3.7 is required.

Execute the following command:

```
python -m flask run --host=0.0.0.0 --port=8082
```

The oracle service is accessible on [localhost:8082/execution-service](http://localhost:8082/execution-service).

## Circuit Execution Request

TODO

`POST /execution-service/`  
```
{  
    TODO
}  
```

## Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss

Dies ist ein Forschungsprototyp.
Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
