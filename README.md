# QuantME-UseCases

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This project contains different use cases for the Quantum Modeling Extension (QuantME), the BPMN extension [Quantum4BPMN](https://github.com/UST-QuAntiL/QuantME-Quantum4BPMN), and the [QuantME Modeling and Transformation Framework](https://github.com/UST-QuAntiL/QuantME-TransformationFramework).

### Electronics 2021 - Special Issue "Quantum Computing System Design and Architecture" - Prototype

In this paper, we demonstrate how to model quantum workflows with Quantum4BPMN independent of a quantum computer to use.
Therefore, the quantum computer is automatically selected during workflow runtime utilizing the [NISQ Analyzer](https://github.com/UST-QuAntiL/nisq-analyzer), and the workflow is dynamically adapted based on reusable workflow fragments depending on the selection.
For this, a workflow model implementing Simon's algorithm and dynamically selecting quantum computers from IBM or a simulator from Rigetti is presented.
The corresponding workflow model, as well as instructions on how to set up the required environment, can be found [here](2021-electronics).

### UCC 2020 - Prototype

In this [paper](https://www.iaas.uni-stuttgart.de/publications/Weder2020_QuantumWorkflows.pdf), we show how to model a workflow using Quantum4BPMN, how to transform it into a native BPMN 2.0-based workflow model, and finally, how to execute the resulting workflow model on the Camunda BPMN engine.
For this, we present three workflow models implementing Simon's algorithm, the Bernstein-Vazirani algorithm, and Grover's algorithm.
The corresponding workflow models can be found [here](2020-ucc).

## Learn More

* Weder, Benjamin; Breitenbücher, Uwe; Leymann, Frank; Wild, Karoline:
  [**Integrating Quantum Computing into Workflow Modeling and Execution**](https://www.iaas.uni-stuttgart.de/publications/Weder2020_QuantumWorkflows.pdf).
  In: Proceedings of the 13th IEEE/ACM International Conference on Utility and Cloud Computing (UCC 2020)

## Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss

Dies ist ein Forschungsprototyp.
Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
