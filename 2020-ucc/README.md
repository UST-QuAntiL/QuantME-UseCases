# UCC 2020 Prototype

This demonstration shows three quantum algorithms modeled as Quantum4BPMN workflow models and transformed into native BPMN 2.0-based workflow models to execute them on the Camunda BPMN engine:

* [Simon's Algorithm](simon)
* [Bernstein-Vazirani's Algorithm](bernstein-vazirani)
* [Grover's Algorithm](grover)

Please refer to the README files in the corresponding folders for details about the quantum algorithms as well as their implementations as workflow models and how to execute them.
Furthermore, in the following, the different steps that have to be performed for the execution of all three workflow models are discussed.

## Usage

### Deploying the Required Services

For the execution of the BPMN 2.0-based workflow models, a set of services providing the required functionality for the different tasks needs to be deployed. 
These services are dockerized and located in [this folder](services). 
Furthermore, the folder contains a docker-compose file, that can be used to easily set up all required service with the following command:

```
docker-compose up -d
```

Please wait until all three services are up and running.

In case you have not installed Docker or Docker-Compose, please refer to the following websites:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker-Compose](https://docs.docker.com/compose/)

Otherwise, the services can also be set up manually. 
Please have a look at the README files in the corresponding folders.

Afterwards, the workflow models implementing the quantum algorithms can be packaged, deployed to a workflow engine, and executed.

### Troubleshooting

The workflow models allow to pass a quantum processing unit (QPU) for the quantum circuit execution through the input parameters.
However, the availability of the QPUs in the [IBM Quantum Experience](https://quantum-computing.ibm.com/) changes sometimes.
Therefore, please check which QPU is currently available and pass its name as input parameter to the workflow engine.
Furthermore, the selected QPU has to satisfy the required number of qubits for the quantum circuits which is defined in the README files of the corresponding folder.

The names of the QPUs displayed in [IBM Quantum Experience](https://quantum-computing.ibm.com/) sometimes differ from the names used in Qiskit.
For example, it displays the name `ibmq_5_yorktown - ibmqx2` but Qiskit uses the name `ibmq_5_yorktown` for this QPU.
Thus, if the execution fails because of an unknown QPU, please check the name using Qiskit, as the implementation relies on this names.