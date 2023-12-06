# Views

The following sections provided detailed information about the quantum, deployment, pattern, and provenance graph views.

## Quantum View

The quantum view utilizes several data source to visualize quantum-specific details.
Device-specific information, such as a quantum devices error rates are retrieved via a provenance system.
Instance-specific information, e.g., the generated circuit, are retrieved from instance data.


| Name                     | Description                                                                      | Context                                                       | Representation      | Data Source       |
|--------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------|---------------------|-------------------|
| circuitVisualization     | graphical representation of the generated circuit                                | quantum circuit loading task                                  | overlay (graphical) | instance data     |
| circuitDepth             | depth the generated circuit                                                      | quantum circuit loading task                                  | overlay (textual)   | instance data     |
| circuitWidth             | number of qubits required by the generated circuit                               | quantum circuit loading task                                  | overlay (textual)   | instance data     |
| qpuName                  | name of the quantum device                                                       | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| queueSize                | queue size of the quantum device                                                 | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| numberOfQubits           | number of qubits provided by the quantum device                                  | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| avgT1Time                | average T1 time of the quantum device's qubits                                   | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| avgT2Time                | average T2 time of the quantum device's qubits                                   | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| avgReadoutError          | average readout error of the quantum device's qubits                             | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| avgSingleQubitGateError  | average single qubit gate error of the quantum device's qubits                   | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| avgMultiQubitGateError   | average multi qubit gate error of the quantum device's qubits                    | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| avgSingleQubitGateTime   | average single qubit gate time of the quantum device's qubits                    | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| avgMultiQubitGateTime    | average multi qubit gate time of the quantum device's qubits                     | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| maxGateTime              | maximum gate time of all qubits of the quantum device                            | quantum circuit execution task, readout error mitigation task | overlay (textual)   | provenance system |
| probabilityDistribution  | probability distribution of the measured solutions                               | quantum circuit execution task, readout error mitigation task | overlay (graphical) | instance data     |
| objectiveValue           | objective value computed on the basis of the measured solutions                  | result evaluation task                                        | overlay (textual)   | instance data     |
| solutionVisualization    | graphical representation of the most commonly measured solution                  | result evaluation task                                        | overlay (graphical) | instance data     |
| optimizedParameters      | the optimized parameters used for the next iteration                             | parameter optimization task                                   | overlay (textual)   | instance data     |
| optimizationLandscape    | visualization of the optimization landscape showcasing the optimization route    | parameter optimization task                                   | overlay (graphical) | instance data     |
| cutCircuitsVisualization | graphical representation of the circuits resulting from applying circuit cutting | circuit cutting task                                          | overlay (graphical) | instance data     |
| numCutCircuits           | number of circuits resulting from applying circuit cutting                       | circuit cutting task                                          | overlay (textual)   | instance data     |
| combinedResult           | number of circuits resulting from applying circuit cutting                       | circuit cutting task                                          | overlay (textual)   | instance data     |


## Deployment View

The deployment view utilize current data provided by the deployment system and the deployed instances.

| Name            | Description                                                 | Context      | Representation      | Data Source       |
|-----------------|-------------------------------------------------------------|--------------|---------------------|-------------------|
| deploymentState | the current status of the deployed instance                 | service task | overlay (textual)   | deployment system |
| topology        | topology of the service instance used by the task           | service task | overlay (graphical) | deployment system |
| nodeProperties  | properties of the nodes contained in the service's topology | service task | overlay (textual)   | deployment system |
| edgeProperties  | properties of the edges contained in the service's topology | service task | overlay (textual)   | deployment system |
| cpu             | CPU used by the instance                                    | service task | overlay (textual)   | deployed instance |
| cpuCores        | CPU cores available to the instance                         | service task | overlay (textual)   | deployed instance |
| ramSize         | memory available to the instance                            | service task | overlay (textual)   | deployed instance |
| diskSize        | storage available to the instance                           | service task | overlay (textual)   | deployed instance |
| cpuUsage        | current usage of the CPU used by the instance               | service task | overlay (textual)   | deployed instance |
| clockSpeed      | current clock speed of the CPU used by the instance         | service task | overlay (textual)   | deployed instance |
| ramUsage        | current usage of the memory used by the instance            | service task | overlay (textual)   | deployed instance |
| diskUsage       | current usage of the disk used by the instance              | service task | overlay (textual)   | deployed instance |


## Pattern View

The pattern view utilizes pattern platform to enrich the workflow with additional details about the pattern.

| Name                                                                                                                                                                                  | Description                                                                                              | Context                                       | Representation      | Data Source      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------|---------------------|------------------|
| [Variational Quantum Algorithm pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/bc795a9b-7977-4e01-b513-f9f5aba38aa7)              | provides insights for variational quantum algorithms when a corresponding circuit was generated          | quantum circuit loading task                  | overlay (reference) | pattern platform |
| [Quantum Approximate Optimization Algorithm pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/da93f915-7f4c-49df-99d0-80d91f26a337) | provides insights about the Quantum Approximate Optimization Algorithm (QAOA)                            | quantum circuit loading task                  | overlay (reference) | pattern platform |
| [Circuit Cutting pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/3d9bca6e-5fca-40c5-b005-8a794958f3aa)                            | provides fundamentals for understanding circuit cutting techniques                                       | circuit cutting task, result combination task | overlay (reference) | pattern platform |
| [Matrix Encoding pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/45d09c54-3f4a-453b-885d-2772443c8d72)                            | provides insights about the matrix encoding technique                                                    | data preparation task                         | overlay (reference) | pattern platform |
| [Initialization pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/312bc9d3-26c0-40ae-b90b-56effd136c0d)                             | provides fundamentals about the initialization of quantum states                                         | data preparation task                         | overlay (reference) | pattern platform |
| [Schmidt Decomposition pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/4437fb83-34c0-47a8-8c6f-1272a76b76bb)                      | provides insights about the schmidt decomposition                                                        | data preparation task                         | overlay (reference) | pattern platform |
| [Basis Encoding pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/bcd4c7a1-3c92-4f8c-a530-72b8b95d3750)                             | provides insights about the basis encoding technique                                                     | data preparation task                         | overlay (reference) | pattern platform |
| [Error Correction pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/1a5e3708-da39-4356-ab3f-115264da6390)                           | provides fundamentals for understanding error correction techniques                                      | error correction task                         | overlay (reference) | pattern platform |
| [Readout Error Mitigation pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/ed3af509-904e-4732-8113-215d65a7d53d)                   | provides fundamentals for understanding readout error mitigation techniques                              | readout error mitigation task                 | overlay (reference) | pattern platform |
| [Amplitude Encoding pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/502147ec-45fa-403f-8f52-e196b3359399)                         | provides insights about the amplitude encoding technique                                                 | data preparation task                         | overlay (reference) | pattern platform |
| [Angle Encoding pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/e595558d-bfea-4b82-9f47-a38a2097b245)                             | provides insights about the angle encoding technique                                                     | data preparation task                         | overlay (reference) | pattern platform |
| [Oracle pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/1cc7e9d6-ab37-412e-8afa-604a25de296e)                                     | describes how oracles are used in quantum algorithms                                                     | oracle expansion task                         | overlay (reference) | pattern platform |
| [QuAM encoding pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/482714a7-8409-4165-93fe-72b02c2ae99c)                              | provides insights about the QuAM encoding technique                                                      | data preparation task                         | overlay (reference) | pattern platform |
| [Priorizted Execution pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/70adfd6f-0648-47cf-88ff-0212b882a262)                       | describes how prioritized execution can be used and in which scenarios they provide benefits             | quantum circuit execution task                | overlay (reference) | pattern platform |
| [QRAM Encoding pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/d9c57511-1101-4707-99bf-36f43a12cb13)                              | provides insights about the QRAM encoding technique                                                      | data preparation task                         | overlay (reference) | pattern platform |
| [Variational Quantum Eigensolver pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/27a5d147-a323-4c6a-84ef-45d80cae923d)            | provides insights about the Variational Quantum Eigensolver (VQE) algorithm                              | quantum circuit loading task                  | overlay (reference) | pattern platform |
| [Warm Starting pattern](https://patterns.platform.planqk.de/pattern-languages/af7780d5-1f97-4536-8da7-4194b093ab1d/3ea9e187-e91b-4852-84eb-b35b5c480892)                              | provides the fundamentals about warm-starting techniques and their application                           | warm-starting task                            | overlay (reference) | pattern platform |
| [Software as a Service pattern](https://patterns.platform.planqk.de/pattern-languages/efdc1625-6445-4662-a37e-5f1fd37a542b/68a4bbc9-2535-4cfc-a4f4-b149adfb674a)                      | provides fundamentals about the Software as a Service pattern and discusses advantages and disadvantages | service task                                  | overlay (reference) | pattern platform |
| [Dedicated Component pattern](https://patterns.platform.planqk.de/pattern-languages/efdc1625-6445-4662-a37e-5f1fd37a542b/da3a0878-df45-4eb1-857e-82e5ae055683)                        | discusses when a dedicated component is beneficial                                                       | service task                                  | overlay (reference) | pattern platform |
| [Platform as a Service pattern](https://patterns.platform.planqk.de/pattern-languages/efdc1625-6445-4662-a37e-5f1fd37a542b/d285eda8-41ee-4ba2-879d-52acec6a1416)                      | provides fundamentals about the Platform as a Service pattern and discusses advantages and disadvantages | service task                                  | overlay (reference) | pattern platform |
| [Private Cloud pattern](https://patterns.platform.planqk.de/pattern-languages/efdc1625-6445-4662-a37e-5f1fd37a542b/b8e826e0-dc07-4515-ae10-87b402e3d52c)                              | provides fundamentals about private clouds                                                               | service task                                  | overlay (reference) | pattern platform |
| [Public Cloud pattern](https://patterns.platform.planqk.de/pattern-languages/efdc1625-6445-4662-a37e-5f1fd37a542b/358bf776-378f-465e-a9e6-e8a1c7716825)                               | provides fundamentals about public clouds                                                                | service task                                  | overlay (reference) | pattern platform |
| [Software as a Service pattern](https://patterns.platform.planqk.de/pattern-languages/efdc1625-6445-4662-a37e-5f1fd37a542b/68a4bbc9-2535-4cfc-a4f4-b149adfb674a)                      | provides fundamentals about the Software as a Service pattern and discusses advantages and disadvantages | service task                                  | overlay (reference) | pattern platform |
| [Provider managed Container Hosting pattern](https://patterns.platform.planqk.de/pattern-languages/ddbd6d47-6a71-4e41-8704-8c313f3e819f/b8785a66-2805-4559-8332-dd348ace3afc)         | discusses the application scenarios for provider managed container hosting                               | service task                                  | overlay (reference) | pattern platform |
| [Provider-managed Scaling Configuration pattern](https://patterns.platform.planqk.de/pattern-languages/ddbd6d47-6a71-4e41-8704-8c313f3e819f/92dddd27-4627-42aa-b667-a9c9d805e475)     | discusses the advantages and disadvantages of provider-managed scaling configurations                    | service task                                  | overlay (reference) | pattern platform |


## Provenance Graph View

