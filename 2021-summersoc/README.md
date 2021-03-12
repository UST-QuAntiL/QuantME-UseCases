# SummerSOC 2021 Prototype

This use case shows how to specify Quantum4BPMN workflow models independent of a quantum computer by using a *QuantumHardwareSelectionSubprocess*.
The quantum computer is then automatically selected during workflow runtime, and the QuantME modeling constructs within the QuantumHardwareSelectionSubprocess are dynamically replaced by suitable workflow fragments based on the selected quantum computer.

The following figure shows a workflow model implementing Simon's algorithm:

![Workflow Model](./workflow/simons-algorithm-hardware-selection.png)

Furthermore, it is available in XML format [here](./workflow/simons-algorithm-hardware-selection.bpmn).
In the following, the different steps to execute the workflow model including the dynamic hardware selection is presented.

## Setting up the Environment

Next, we will discuss the steps required to set-up the environment to model and execute the workflow model.

### Running the QuantME Transformation Framework

First, build and run the [QuantME Transformation Framework](https://github.com/UST-QuAntiL/QuantME-TransformationFramework):

1. Clone the repository using release v1.2.0: 
```
git clone https://github.com/UST-QuAntiL/QuantME-TransformationFramework.git --branch v1.2.0
```
2. Change to the cloned folder and build the framework:
```
npm install
npm run build
```
3. The build product can be found in the ``dist`` folder and started depending on the operating system, e.g., using the ``.exe`` for Windows

The QuantME Transformation Framework can be configured on start-up by passing in corresponding environment variables. 
However, we will update the configuration using the graphical user interface:

Open the configuration window:

![Configuration](./docs/open-settings.png)

Update the different configuration properties using the following values.
Thereby, $IP has to be replaced with the IP-address of the Docker engine if you use the Docker setup (see bellow):

* ``Camunda Engine Endpoint``: http://$IP:8080/engine-rest
* ``OpenTOSCA Endpoint``: http://$IP:1337/csars
* ``Winery Endpoint``: http://$IP:8093/winery
* ``QRM Repository User``: UST-QuAntiL
* ``QRM Repository Name``: QuantME-UseCases
* ``QRM Repository Path``: /2021-summersoc/QRMs

![Update Configuration](./docs/update-settings.png)

### Running the OpenTOSCA and QuAntiL Components

All other required service can be started using the Docker-Compose file located in [this folder](./docker):

1. Update the [.env](./docker/.env) file with your settings: 
  * ``PUBLIC_HOSTNAME``: Enter the hostname/IP address of your Docker engine. Do *not* use ``localhost``.
  * ``IBM_ACCESS_TOKEN``: Enter your IBM access token which is needed to retrieve the required provenance data by [QProv](https://github.com/UST-QuAntiL/qprov). It can be retrieved using the [IBM Quantum Experience](https://quantum-computing.ibm.com/) UI.

2. Run the Docker-Compose file:
```
docker-compose pull
docker-compose up --build
```

3. Wait until all containers are up and running. This may take some minutes.

## Model the Workflow and Transform it to Native BPMN

Next, the workflow model implementing Simon's algorithm is imported into QuantME Transformation Framework:

* Click on ``File`` in the top-left corner of the QuantME Transformation Framework
* Select ``Open File...``
* Navigate to the workflow model available in this repository (see [here](./workflow/simons-algorithm-hardware-selection.bpmn)) and open it

The workflow model should now be visible in the QuantME Transformation Framework:

![Imported Workflow](./docs/import-workflow.png)

TODO

## Execute the Workflow using the Camunda Engine

TODO
