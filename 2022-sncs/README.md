# Springer Nature Computer Science 2022 Prototype

Different hybrid quantum algorithms require the interleaved execution of quantum and classical programs in a hybrid loop, e.g., the [Quantum Approximate Optimization Algorithm (QAOA)](https://arxiv.org/abs/1411.4028) or the [Variational Quantum Eigensolver (VQE)](https://www.nature.com/articles/nature23879?sf114016447=1).
For these algorithms, the orchestration using workflows can be ineffiecient due to queing and data transmission times summing up over multiple iterations.
Thus, so-called *hybrid runtimes*, such as the [Qiskit Runtime](https://quantum-computing.ibm.com/lab/docs/iql/runtime/) or [AWS Braket Hybrid Jobs](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs.html), were developed hosting the quantum and classical programs for such algorithms and optimizing their execution.
In this use case, we show how to model quantum workflows independently of a certain hybrid runtime, analyze them to find workflow fragments that can benefit from hybrid runtimes, and rewrite the workflow to use these runtimes instead of orchestrating the hybrid loops.
However, rewriting the workflow leads to a difficult monitoring and analysis of workflow executions, as the modeled and executed workflows differ.
Hence, process views are utilized to visualize the modeled and executed workflow within the workflow engine depending on the user needs.

Furthermore, also a demo video showing the different steps of this tutorial is available on [YouTube](TODO).

In the following sections, we present the analysis and rewrite method based on the workflow model shown below:

![Exemplary Quantum Workflow](./docs/exemplary-quantum-workflow.png)

First, [pre-processed data](./data/embedding-10.txt) is loaded, which is used to initialize a quantum k-means algorithm.
Then, the workflow enters a hybrid loop, executing quantum circuits, calculating new centroids based on the results, and adapting the quantum circuits if needed for the next iteration.
This loop ends when the clustering converges, i.e., the difference between the new and old centroids is smaller than a given threshold or the maximum number of iterations is reached.
Next, a variational support vector machine is trained.
This is done using another hybrid loop, optimizing the parameters theta until the incurred costs are smaller than 0.3 or the limit of 10 iterations is reached.
Finally, the variational support vector machine is evaluated by classifying test data, and the resulting figure is displayed to the user in the last user task.

In case you experience any problems during modeling, rewrite, deployment, or execution of the workflow, please refer to the [Troubleshooting](#troubleshooting) section at the end of this README.

The use case utilizes the MODULO framework, comprising the following components, for which more details can be found in their corresponding Github repositories:

* [QuantME Modeling and Transformation Framework](https://github.com/UST-QuAntiL/QuantME-TransformationFramework): A graphical BPMN modeler to define quantum workflows, as well as analyzing and rewriting them for the usage of hybrid runtimes.
* [Camunda Process View Plugin](https://github.com/UST-QuAntiL/camunda-process-views-plugin): A plugin for the [Camunda engine](https://camunda.com/platform-7/workflow-engine) enabling to visualize process views for quantum workflows.
* [Qiskit Runtime Handler](https://github.com/UST-QuAntiL/qiskit-runtime-handler): A handler generating Qiskit Runtime programs based on a given workflow fragments orchestrating a hybrid loop.
* [Winery](https://github.com/OpenTOSCA/winery): A graphical modeler for TOSCA-based deployment models.
* [OpenTOSCA Container](https://github.com/OpenTOSCA/container): A standard-compliant deployment system for TOSCA-based deployment models.

## Setting up the MODULO Framework

First, we will discuss the steps required to set up the different components of the MODULO framework.
All components except the QuantME Modeling and Transformation Framework, providing the graphical BPMN modeler, are available via Docker.
Therefore, these components can be started using the Docker-Compose file available [here](./docker):

1. Update the [.env](./docker/.env) file with your settings: 
  * ``PUBLIC_HOSTNAME``: Enter the hostname/IP address of your Docker engine. Do *not* use ``localhost``.

2. Run the Docker-Compose file:
```
docker-compose pull
docker-compose up --build
```

3. Wait until all containers are up and running. This may take some minutes.

To start the QuantME Modeling and Transformation Framework, please execute the following steps:

1. Clone the repository using release v1.6.0: 
```
git clone https://github.com/UST-QuAntiL/QuantME-TransformationFramework.git --branch v1.6.0
```

2. Move to the cloned folder and build the framework:
```
npm install
npm run build
```

3. The build product can be found in the ``dist`` folder and started depending on the operating system, e.g., using the ``.exe`` for Windows.

Afterwards, the following screen should be displayed:

![QuantME Transformation Framework](./docs/modeler-after-build.png)

Open the example workflow model available [here](./workflow/analysis-and-rewrite-workflow.bpmn) using the QuantME Modeling and Transformation Framework.
For this, click on ``File`` in the top-left corner, and afterwards, select the workflow model in the dialogue ``Open File...``.
Then, the following screen is displayed:

![Quantum Workflow in Modeler](./docs/quantum-workflow-in-modeler.png)

The QuantME Modeling and Transformation Framework must be configured with the endpoints of the services for the deployment and the hybrid program generation.
For this, click on ``Configuration`` in the toolbar, opening the config pop-up:

![Quantum Workflow in Modeler](./docs/modeler-configuration.png)

Please update the different configuration properties using the following values.
Thereby, $IP has to be replaced with the IP-address of the Docker engine used for the setup described above:

* ``BPMN`` tab:
    * ``Camunda Engine Endpoint``: http://$IP:8080/engine-rest
* ``OpenTOSCA`` tab:
    * ``OpenTOSCA Endpoint``: http://$IP:1337/csars
    * ``Winery Endpoint``: http://$IP:8093/winery
* ``QRM Data`` tab:
    * ``QRM Repository User``: UST-QuAntiL
    * ``QRM Repository Name``: QuantME-UseCases
    * ``QRM Repository Path``: 2022-sncs/qrms
* ``Hybrid Runtimes`` tab:
    * ``Qiskit Runtime Handler Endpoint``: http://$IP:8889
    * ``Retrieve Intermediate Results``: Tick the checkbox

In case you want to execute the workflow model without optimization, press the ``Transformation`` Button in the toolbar on the top to retrieve a standard-compliant BPMN workflow model.
Then, directly go to the [Deploying the Required Services](#deploying-the-required-services) section.
However, do *not* perform the transformation if you want to optimize the workflow, as this has to be done before the transformation step.

## Analysis and Rewrite of Quantum Workflows

TODO