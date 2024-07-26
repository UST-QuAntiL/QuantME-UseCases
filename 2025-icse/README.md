# ICSE 2025 Prototype

Building quantum applications requires deep knowledge of quantum computing and software engineering.
Hence, an abstraction layer reducing the complexity for non-experts is required.
Patterns are an established concept for abstractly describing proven solution strategies to recurring problems.
Therefore, the quantum computing patterns, a pattern language for the quantum computing domain, can be used to define the building blocks and the structure of hybrid quantum applications.
Furthermore, concrete software artifacts can be associated with patterns to solve the corresponding problem.
However, these software artifacts are usually heterogeneous, e.g., using different data formats.
Quantum workflows enable a robust and scalable orchestration of these heterogeneous software artifacts.
However, manually modeling and configuring such quantum workflows is a complex, error-prone, and time-consuming task.
To overcome this issue, we present an approach that automates the generation and adaptation of quantum workflows utilizing the quantum computing patterns.

In the following sections, we showcase our pattern-based generation and adaptation approach for an exemplary variational quantum algorithm that solves the Maximum Cut (MaxCut) problem using the [Quantum Approximate Optimization Algorithm (QAOA)](https://arxiv.org/pdf/1411.4028.pdf).

A video showcasing the described use case is available on YouTube:

[![IMAGE ALT TEXT HERE](TODO)](TODO)

A table with the runtime evaluation can be found [here](https://github.com/UST-QuAntiL/QuantME-UseCases/blob/master/2025-icse/evaluation-data/runtime-evaluation.xlsx).

An overview of the patterns, their categorization, as well as the corresponding paper they were published in can be found [here](https://github.com/UST-QuAntiL/QuantME-UseCases/blob/master/2025-icse/PatternCategories.md)


The use case utilizes the following components:

* [Quantum Workflow Modeler](https://github.com/PlanQK/workflow-modeler): A graphical BPMN modeler to define, transform, and deploy quantum workflows.
* [Quokka](https://github.com/UST-QuAntiL/Quokka): A microservice ecosystem enabling a service-based execution of quantum algorithms.
* [Camunda BPMN Engine](https://camunda.com/products/camunda-platform/bpmn-engine/): A state-of-the-art BPMN workflow engine used to execute quantum workflows after transforming them to native BPMN workflow models to avoid the need for extending the workflow engine.
* [Winery](https://github.com/OpenTOSCA/winery): Winery is a web-based environment to graphically model TOSCA-based deployment models, which can then be attached to activities of quantum workflows to enable their automated deployment in the target environment.
* [OpenTOSCA Container](https://github.com/OpenTOSCA/container): A TOSCA-compliant deployment system to deploy and manage applications or services.
* [Script Splitter](TODO): A service for splitting monolithic quantum computing scripts into a loosely coupled quantum workflow.


## Setup

TODO

## Disclaimer of Warranty
Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss
Dies ist ein Forschungsprototyp. Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
