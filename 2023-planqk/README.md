# Setup the Repository
### Prerequisites:

* Git
* Docker and Docker Compose

### Run the repository:
```
docker-compose pull
docker-compose --profile all up
```

### Profiles

You can use one or multiple of the following profiles to select which containers to start:

| profile  | content          |
|----------|------------------|
| all      | everything       |
| workflow | Workflow Modeler |
| pattern  | Pattern Atlas    |
| nisq     | NISQ Analyzer    |
| qhana    | QHAna            |

To use multiple profiles at once, use multiple profile flags e.g. `--profile workflow --profile pattern`.

## Haftungsausschluss

 Dies ist ein Forschungsprototyp.
 Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.

 ## Disclaimer of Warranty

 Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
 You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.
