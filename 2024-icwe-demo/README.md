# CCIS 2023 Prototype

Variational Quantum Algorithms (VQAs) comprise various complex reoccurring tasks that are not part of the original set of [QuantME modeling constructs](https://www.iaas.uni-stuttgart.de/publications/Weder2020_QuantumWorkflows.pdf), e.g., parameter optimization or objective function evaluation.
As the lack of modeling support for these tasks complicates the process of modeling VQAs in workflows, we developed an extension for QuantME that introduces a new set of modeling constructs specifically tailored for VQAs.

In the following sections, we showcase how these new QuantME4VQA modeling constructs can be used to model and execute an exemplary VQA that solves the Maximum Cut (MaxCut) problem using the [Quantum Approximate Optimization Algorithm (QAOA)](https://arxiv.org/pdf/1411.4028.pdf).

The use case utilizes the Quantum Workflow Modeler and Quokka:

* [Quantum Workflow Modeler](https://github.com/PlanQK/workflow-modeler): A graphical BPMN modeler to define, transform, and deploy quantum workflows.
* [Quokka](https://github.com/UST-QuAntiL/Quokka): A microservice ecosystem enabling a service-based execution of quantum algorithms.

## Setup

First, we will discuss the steps required to set up the different components.
All components are available via Docker.
Therefore, these components can be started using the Docker-Compose file available [here](./docker):

1. Update the [.env](./docker/.env) file with your settings:
  * ``PUBLIC_HOSTNAME``: Enter the hostname/IP address of your Docker engine. Do *not* use ``localhost``.

2. Run the Docker-Compose file:
```
docker-compose pull
docker-compose up --build
```

3. Wait until all containers are up and running. This may take some minutes.

Open the Quantum Workflow Modeler using the following URL: [localhost:8080](http://localhost:8080)

Afterwards, the following screen should be displayed:

![Modeler Initial](./docs/modeler-initial.png)

Open the example workflow model available [here](./workflow/workflow_casestudy.bpmn) using the Quantum Workflow Modeler.
For this, click on ``Open`` in the top-left corner, and afterwards, select the workflow model in the dialogue ``Open File...``.
Then, the following screen is displayed:

![Quantum Workflow in Modeler](./docs/modeler-workflow-loaded.png)

The Quantum Workflow Modeler is pre-configured with the endpoints of the workflow engine and the QRM repository.
To check these settings, click on ``Configuration`` in the toolbar, opening the config pop-up:

![Quantum Workflow in Modeler](./docs/modeler-configuration.png)

Please verify that the different configuration properties are set to the following values.
Thereby, $IP has to be replaced with the IP-address of the Docker engine used for the setup described above:

* Under ``Editor``:
    * ``Camunda Engine Endpoint``: http://$IP:8080/engine-rest
* Under ``QRM Data``:
    * ``QRM Repository User``: UST-QuAntiL
    * ``QRM Repository Name``: QuantME-UseCases
    * ``QRM Repository Path``: 2023-ccis/qrms


### Configuring, Transforming, and Executing the Quantum Workflow

The imported workflows starts of with a warm-starting task, which is used to approximate a solution that is incorporated into the quantum circuit to facilitate the search for the optimal solution.
Next, it generates a parameterized QAOA circuit for MaxCut.
This circuit, is then cut into smaller sub-circuits by the circuit cutting sub-process, which are subsequently executed.
Afterwards, the results of the sub-circuits are combined to construct the original circuit's result.
This result is evaluated and used to optimize the QAOA parameters, starting another iteration of the loop.
Once the optimization is converged, the result is returned to the user for analysis.

QuantME4VQA enables the configuration of the warm-starting, optimization and circuit-cutting via the properties panel (see on the right).

![QuantME4VQA Properties](./docs/modeler-properties.png)

To execute the workflow, the QuantME and QuantME4VAR modeling constructs must be replaced by standard-compliant BPMN modeling constructs.
Therefore, click on the ``Transform Workflow`` button.

![Quantum Workflow Modeler](./docs/modeler-transformation.png)

The resulting native workflow model, that will automatically be opened in a new tab, is displayed below.
For example, the Warm-Starting Task and Quantum Circuit Loading Task are replaced by two Service Tasks invoking the corresponding services of the Quokka ecosystem based on the configuration attributes.
Additionally, new Service Tasks are inserted to split the quantum circuit, as well as to combine the results after the execution.

![Quantum Workflow Modeler](./docs/modeler-transformed-workflow.png)

Next, deploy the workflow by clicking the ``Deploy Workflow`` button.

![Quantum Workflow Modeler](./docs/modeler-deploy-workflow.png)

Open the Camunda Engine using the following URL: [localhost:8090](http://localhost:8090)
Use ``demo`` as username and password to log in, which displays the following screen:

![Camunda Loginscreen](./docs/camunda-loginscreen.png)

Click on the home icon in the top-right corner and select ``Cockpit`` to validate that the workflow was successfully uploaded.
Then, click on ``Processes`` on the top-left and select the workflow from the list.
This should show a graphical representation of the uploaded workflow:

![Camunda Workflow Overview](./docs/camunda-wfoverview.png)

To instantiate the workflow, click the home button on the top-right, then select ``Tasklist``.
Next, click on ``Start process`` on the top-right, select the name of the uploaded workflow, and provide the input parameters as shown below:

* ``adjMatrix``: ``[[0,2,1],[3,0,1],[1,2,0]]``
* ``betas``: ``[1]``
* ``gammas``: ``[1]``
* ``token``: ``YOUR_IBMQ_TOKEN`` (can be left empty when using the aer simulator (default))

![Camunda Start Process](./docs/camunda-startprocess.png)

The UI displays a notification at the bottom-right that the workflow instance was successfully started.
Afterwards, once more, click on the home icon on the top-right and select Cockpit. 
Click on the Running Process Instance, select the started workflow, and then click on the workflow ID. 
Now the workflow's token flow and the changing variables can be observed. To see the current state of the workflow instance refresh the page.

![Camunda Start Process](./docs/camunda-running-workflow.png)

Wait until the token reaches the final user task in the workflow, as depicted below.
This might take some time, depending on the circuit size, the execution parameters, and the utilization of the selected quantum device or simulator.

![Camunda Start Process](./docs/camunda-processfinished.png)

Switch to the Tasklist.
Select the task item on the left (1), then click on ``Claim`` to activate the item (2), and download the result plot using the given URL (3).
Finally, click the ``Complete`` button (4) to finish the human task, and as it is the last activity in the workflow, to terminate the workflow instance.

![Camunda Analyze Results](./docs/camunda-analyzeresults.png)

Open the downloaded image, visualizing the MaxCut solution for the input graph.

![Max Cut Plot](./docs/maxcut-plot.png)

## Disclaimer of Warranty
Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss
Dies ist ein Forschungsprototyp. Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
