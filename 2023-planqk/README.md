# Setup the Repository
### Prerequisites:

* Git
* Docker and Docker Compose

### University of Stuttgart network

If you are in the network of the University of Stuttgart, the `apt` command might fail.
To fix that, write the DNS of the network into the resolv.conf file and remove the leading underscore in the file name of `_docker-compose.overwrite.yml`.

### SSH key for private content repositories

The database can fill itself automatically with example data.
To activate this you need to create a SSH key that you link with GitHub and copy the private key to the current folder and name the file `ssh_secret`.


### Run the repository:

Download and pull the necessary images:

```
docker compose --profile all pull --ignore-buildable
docker compose build
```

The database needs to import data and start up before you can start the other containers.
To accomplish this, first run:

```
docker compose up db -d
```

Wait till the database has finished importing data and is ready, then run:

```
docker compose --profile all up
```

### UI URLs

You can access the different UIs under the following URLs:

| UI               | port                  |
|------------------|-----------------------|
| QC Atlas         | http://localhost:8060 |
| Pattern Atlas    | http://localhost:1978 |
| NISQ Analyzer    | http://localhost:5009 |
| Workflow Modeler | http://localhost:8061 |
| Camunda          | http://localhost:8090 |
| OpenTOSCA UI     | http://localhost:8088 |
| Winery           | http://localhost:8080 |

### Profiles

You can use one or multiple of the following profiles to select which containers to start:

| profile  | content          |
|----------|------------------|
| all      | everything       |
| qcatlas  | QC Atlas         |
| workflow | Workflow Modeler |
| pattern  | Pattern Atlas    |
| nisq     | NISQ Analyzer    |
| tosca    | OpenTOSCA        |
| quokka   | Quokka           |

To use multiple profiles at once, use multiple profile flags e.g. `--profile workflow --profile pattern`.

## Troubleshooting

### invalid mount config for type "bind": bind source path does not exist: .../QuantME-UseCases/2023-planqk/ssh_secret

Add an SSH key as described [here](#ssh-key-for-private-content-repositories) or just create an empty file named `ssh_secret`.

## Haftungsausschluss

 Dies ist ein Forschungsprototyp.
 Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.

 ## Disclaimer of Warranty

 Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
 You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.
