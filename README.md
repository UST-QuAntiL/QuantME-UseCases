# Quantum Workflows, MODULO, and QuantME Use Cases

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This project contains different use cases for quantum workflows and the MODULO framework.
Thereby, the MODULO framework incorporates the Quantum Modeling Extension (QuantME) and the corresponding BPMN extension [Quantum4BPMN](https://github.com/UST-QuAntiL/QuantME-Quantum4BPMN).
Furthermore, it provides an integrated toolchain to model, transform, deploy, and execute quantum workflows comprising the following components:

* [QuantME Modeling and Transformation Framework](https://github.com/UST-QuAntiL/QuantME-TransformationFramework): A graphical BPMN modeler supporting Quantum4BPMN to ease the modeling of quantum workflows by providing explicit modeling constructs for the execution of quantum circuits, as well as frequently occurring pre- and post-processing tasks. Furthermore, it enables transforming quantum workflows using Quantum4BPMN modeling constructs to native BPMN workflows to retain their portability between different workflow engines. Finally, it integrates the other components of the MODULO framework to automatically deploy required services, bind them to a workflow, and upload the executable workflow to a workflow engine.
* [Camunda BPMN Engine](https://camunda.com/products/camunda-platform/bpmn-engine/): A state-of-the-art BPMN workflow engine used to execute quantum workflows after transforming them to native BPMN workflow models to avoid the need for extending the workflow engine.
* [Winery](https://github.com/OpenTOSCA/winery): Winery is a web-based environment to graphically model TOSCA-based deployment models, which can then be attached to activities of quantum workflows to enable their automated deployment in the target environment.
* [OpenTOSCA Container](https://github.com/OpenTOSCA/container): A TOSCA-compliant deployment system to deploy and manage applications or services.

### ICWS 2021 - Prototype

In this paper, we motivate the need for two orchestrations that are required to implement non-trivial hybrid quantum applications:
(i) the orchestration of the data- and control flow between the different components comprising the application, and (ii) the orchestration of the provisioning of the execution environment required by the application.
We motivate this by a use case from the humanities, performing data preparation, clustering, and classification on costume data.
Thereby, the [OpenTOSCA ecosystem](https://github.com/OpenTOSCA) is used to automatically provision the corresponding execution environment.
Furthermore, the [Camunda BPMN engine](https://camunda.com/products/camunda-platform/bpmn-engine/) is utilized to execute the workflow orchestrating the data- and control flow.
The corresponding workflow model, topology model, as well as instructions on how to set up the required environment and execute the hybrid quantum application are available [here](2021-icws).

### Electronics 2021 - Special Issue "Quantum Computing System Design and Architecture" - Prototype

In this [paper](https://www.mdpi.com/2079-9292/10/8/984), we demonstrate how to model quantum workflows with Quantum4BPMN independent of a quantum computer to use.
Therefore, the quantum computer is automatically selected during workflow runtime utilizing the [NISQ Analyzer](https://github.com/UST-QuAntiL/nisq-analyzer), and the workflow is dynamically adapted based on reusable workflow fragments depending on the selection.
For this, a workflow model implementing Simon's algorithm and dynamically selecting quantum computers from IBM or a simulator from Rigetti is presented.
The corresponding workflow model, as well as instructions on how to set up the required environment, can be found [here](2021-electronics).

### UCC 2020 - Prototype

In this [paper](https://www.iaas.uni-stuttgart.de/publications/Weder2020_QuantumWorkflows.pdf), we show how to model a workflow using Quantum4BPMN, how to transform it into a native BPMN 2.0-based workflow model, and finally, how to execute the resulting workflow model on the Camunda BPMN engine.
For this, we present three workflow models implementing Simon's algorithm, the Bernstein-Vazirani algorithm, and Grover's algorithm.
The corresponding workflow models can be found [here](2020-ucc).

## Learn More

* Weder, Benjamin; Barzen, Johanna; Leymann, Frank; Zimmermann, Michael: 
  Hybrid Quantum Applications Need Two Orchestrations in Superposition: A Software Architecture Perspective. 
  In: Proceedings of the 18th IEEE International Conference on Web Services (ICWS 2021)

* Weder, Benjamin; Barzen, Johanna; Leymann, Frank; Salm, Marie:
  [**Automated Quantum Hardware Selection for Quantum Workflows**](https://www.mdpi.com/2079-9292/10/8/984/pdf).
  In: Electronics 2021, 10(8), 984

* Weder, Benjamin; Breitenbücher, Uwe; Leymann, Frank; Wild, Karoline:
  [**Integrating Quantum Computing into Workflow Modeling and Execution**](https://www.iaas.uni-stuttgart.de/publications/Weder2020_QuantumWorkflows.pdf).
  In: Proceedings of the 13th IEEE/ACM International Conference on Utility and Cloud Computing (UCC 2020)

## Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss

Dies ist ein Forschungsprototyp.
Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
