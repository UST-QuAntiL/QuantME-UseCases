# Provenance-Service

Service to mitigate the given results by using a defined unfolding technique.

## Setup

Install packages as listed in [requirements.txt](requirements.txt). 
Python 3.7 is required.

Execute the following command:

```
python -m flask run --host=0.0.0.0 --port=8083
```

The provenance service is accessible on [localhost:8083/provenance-service](http://localhost:8083/provenance-service).

## Readout-Error Mitigation Request

Send CorrelationId, ReturnAddress, QPU, UnfoldingTechnique, MaxAge, and Result to the API to mitigate the error in the given result distribution and to receive the mitgated result at the specified address via POST.

`POST /provenance-service/`  
```
{  
    "CorrelationId": "Unique Id that is returned in the response to correlate it with the request",
    "ReturnAddress": "The address to send the mitigated result to",
    "QPU": "The name of the QPU that was used for the execution",
    "UnfoldingTechnique": "The name of the unfolding technique to use for the mitigation",
    "MaxAge": "The maximum allowed age of the error model to use for the mitigation (in minutes)",
    "Result": "The result distribution to mitigate"
}  
```

## Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss

Dies ist ein Forschungsprototyp.
Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
