# DH 2026

This repository accompanies the DH 2026 paper and provides a research prototype of the **Multi-Domain Quantum Low-Code Modeler** together with a complete execution environment for domain-specific quantum low-code models.

The artifact demonstrates how domain experts can model optimization problems (e.g., finance) using high-level abstractions and execute the resulting hybrid quantum-classical workflows based on QAOA.

---

## Overview

The system consists of the following components:

- **Quantum Low-Code Modeler**  
  A web-based graphical modeling environment that enables users to construct quantum applications using domain-specific abstractions rather than low-level quantum circuits. It provides visual elements (domain blocks) representing tasks, constraints, and data, allowing domain experts to specify problems at a high level of abstraction.

- **Backend Transformation Service**  
  A service that automatically transforms them into executable quantum workflows.

- **Agent Context Components**  
  Supporting modules that provide runtime information required for adaptive workflow execution. These components maintain metadata, constraints, and available algorithmic options, enabling an agent to dynamically select suitable implementations during execution while ensuring semantic validity.

- **Camunda Components**  
  The workflow execution environment based on the Camunda platform. It executes the generated BPMN workflows, coordinates interactions between classical services and quantum tasks, manages process state, and provides monitoring tools such as Tasklist and Cockpit for user interaction and result inspection.

---

## 1. Start the Components

Rename the .env.template file to .env and run the following commands from the `docker` directory to start all components:

```
docker-compose pull
docker-compose up --build
```

Wait until all containers are running. This may take several minutes.


## 2. Start Ollama

Camunda currently only supports OpenAI Ollama models and Amazon Bedrock.
Since the execution with Amazon Bedrock can become quite expensive, we advice to use Ollama with the OpenAI model (gpt-oss:20b) if you have enough RAM (32 GB should be enough).

---

## 3. Open the Quantum Low-Code Modeler

Open the Quantum Low-Code Modeler at http://localhost:4242.

You should see the Modeler start screen:

![Modeler Initial](docs/graphics/0_ModelerOverview.png)

---

## 4. Import the Domain Profile

Click on "Manage Domain Profiles" inside the Quantum Low-Code Modeler as depicted here:

![Manage Domain Profiles](docs/graphics/1_ManageDomainProfileButton.png)

Then click on "Import Domain Profile", select the ![finance domain profile](profiles/financeProfile.json) and click on "save":
![Import Domain Profile](docs/graphics/3_DomainProfileImportSuccess.png)

---


## 5. Select the Domain Profile and import the Model

Select the finance profile inside the Experience Mode and import the ![model](models/financeModel.json).
![Import Domain Profile](docs/graphics/4_SelectDomainProfile.png)

After loading, the model should resemble the example shown below.
![Import Model](docs/graphics/5_ModelImport.png)

---

## 6. Transform the Model

Click "Send to Backend" to transform the domain model into an executable workflow.
![Transform](docs/graphics/6_Transformation.png)

---

## 7. Transform the Model

Click "History" and download the result file.
![Download Result](docs/graphics/7_WorkflowDownload.png)

Alternatively, the files can be found in the workflow directory.

---

## 8. Camunda Upload

Open the Camunda Modeler at http://localhost:8070.
Log in using the following credentials:

```
user: demo
password: demo
```


Create a project and upload all files from the ![workflow](workflows/) folder.
This folder contains:

- BPMN workflow
- Agent context file
- Agent feedback loop file

![Upload Files](docs/graphics/9_CamundaSuccessUpload.png)

---

## 9. Execute the Workflow in Camunda

Click on the workflow and click on play.
![Upload Files](docs/graphics/10_CamundaAgentPrompt.png)

---

## 10. View the Result

Open the Camunda Cockpit.

The result includes the asset selection for the four assets and a budget of 2.
Here, QAOA was chosen by the agent and the algorithm finds the following asset selection

```
```
![Final Result](docs/graphics/11_CamundaResult.png)
---



## Disclaimer of Warranty
Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss
Dies ist ein Forschungsprototyp. Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
