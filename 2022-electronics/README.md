# TODO Prototype

TODO: Intro

## Setting up the MODULO Framework 
--> TODO: adapt with specific details

First, we will discuss the steps required to set up the different components comprising the MODULO framework.
All components except the [QuantME Transformation Framework](https://github.com/UST-QuAntiL/QuantME-TransformationFramework) providing the graphical BPMN modeler are available via Docker.
Therefore, these components can be started using the Docker-Compose file available [here](./docker):

1. Update the [.env](./docker/.env) file with your settings: 
  * ``PUBLIC_HOSTNAME``: Enter the hostname/IP address of your Docker engine. Do *not* use ``localhost``.

2. Run the Docker-Compose file:
```
docker-compose pull
docker-compose up --build
```

3. Wait until all containers are up and running. This may take some minutes.

To start the QuantME Transformation Framework, please execute the following steps:

1. Clone the repository using release v1.4.1: 
```
git clone https://github.com/UST-QuAntiL/QuantME-TransformationFramework.git --branch v1.4.1
```

2. Move to the cloned folder and build the framework:
```
npm install
npm run build
```

3. The build product can be found in the ``dist`` folder and started depending on the operating system, e.g., using the ``.exe`` for Windows.

Afterwards, the following screen should be displayed:

![QuantME Transformation Framework](./docs/modeler-after-build.png)

Open the example workflow model available [here](./workflow/analysis-and-rewrite-workflow.bpmn) using the QuantME Transformation Framework.
For this, click on ``File`` in the top-left corner, and afterwards, select the workflow model in the dialogue ``Open File...``.
Then, the following screen is displayed:

![Quantum Workflow in Modeler](./docs/quantum-workflow-in-modeler.png)

The QuantME Transformation Framework must be configured with the endpoints of the services for the deployment and the hybrid program generation.
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
    * ``QRM Repository Path``: 2022-closer/qrms
* ``Hybrid Runtimes`` tab:
    * ``Qiskit Runtime Handler Endpoint``: http://$IP:8889

In case you want to execute the workflow model without optimization, press the ``Transformation`` Button in the toolbar on the top to retrieve a standard-compliant BPMN workflow model.
Then, directly go to the [Deploying the Required Services](#deploying-the-required-services) section.
However, do *not* perform the transformation if you want to optimize the workflow, as this has to be done before the transformation step.

TODO: add use-case description