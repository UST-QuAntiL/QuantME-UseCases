# Quantum Workflows, MODULO, and QuantME Use Cases

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This project contains different use cases for quantum workflows and the MODULO framework.
Thereby, the MODULO framework incorporates the Quantum Modeling Extension (QuantME) and the corresponding BPMN extension [Quantum4BPMN](https://github.com/UST-QuAntiL/QuantME-Quantum4BPMN).
Furthermore, it provides an integrated toolchain to model, transform, deploy, and execute quantum workflows comprising the following components:

* [Quantum Workflow Modeler](https://github.com/PlanQK/workflow-modeler) (previously [QuantME Modeling and Transformation Framework](https://github.com/UST-QuAntiL/QuantME-TransformationFramework)): A graphical BPMN modeler supporting Quantum4BPMN to ease the modeling of quantum workflows by providing explicit modeling constructs for the execution of quantum circuits, as well as frequently occurring pre- and post-processing tasks. Furthermore, it enables transforming quantum workflows using Quantum4BPMN modeling constructs to native BPMN workflows to retain their portability between different workflow engines. Finally, it integrates the other components of the MODULO framework to automatically deploy required services, bind them to a workflow, and upload the executable workflow to a workflow engine.
* [Camunda BPMN Engine](https://camunda.com/products/camunda-platform/bpmn-engine/): A state-of-the-art BPMN workflow engine used to execute quantum workflows after transforming them to native BPMN workflow models to avoid the need for extending the workflow engine.
* [Winery](https://github.com/OpenTOSCA/winery): Winery is a web-based environment to graphically model TOSCA-based deployment models, which can then be attached to activities of quantum workflows to enable their automated deployment in the target environment.
* [OpenTOSCA Container](https://github.com/OpenTOSCA/container): A TOSCA-compliant deployment system to deploy and manage applications or services.
* [Qiskit Runtime Handler](https://github.com/UST-QuAntiL/qiskit-runtime-handler): A service generating Qiskit Runtime programs for hybrid loops based on corresponding workflow fragments detected by the QuantME Modeling and Transformation Framework.
* [AWS Braket Hybrid Jobs Handler](https://github.com/UST-QuAntiL/amazon-braket-hybrid-jobs-handler): A service generating AWS Braket Hybrid Jobs programs for hybrid loops based on corresponding workflow fragments detected by the QuantME Modeling and Transformation Framework.
* [Script Splitter](https://github.com/UST-QuAntiL/qscript-splitter): A service analyzing Python scripts to detect quantum and classical parts, which are then orchestrated by a generated workflow model.

### CCIS 2023 - Prototype

In this paper, we extend our [CLOSER 2023 paper](https://www.iaas.uni-stuttgart.de/publications/Beisel2023_QuantME4VQA.pdf), defining a metamodel for quantum workflows and formalizing the transformation of QuantME modeling constructs to native modeling constructs.
The metamodel is used to introduce quantum-specific workflow modeling constructs that facilitate the modeling of Variational Quantum Algorithms (VQAs) as quantum workflows.
To demonstrate the functionality of our modeling extension, we implemented a case study solving the Maximum Cut (MaxCut) problem using the Quantum Approximate Optimization Algorithm (QAOA).
The corresponding workflow models and instructions on how to set up the environment and execute the application can be found [here](2023-ccis).

### ICWE 2023 - Tutorial

In this tutorial, we show how to model, transform, deploy, execute, and monitor a real-world hybrid quantum application using workflows.
Thereby, the [Quokka ecosystem](https://github.com/UST-QuAntiL/Quokka), as well as the [quantum workflow modeler](https://github.com/PlanQK/workflow-modeler), are utilized.
The hybrid quantum application uses multiple quantum algorithms, as well as multiple classical programs, to solve a use case from the package delivery domain.
Detailed instructions for the use case are available [here](https://ust-quantil.github.io/icwe-tutorial/handson.html), and the required code can be accessed [here](2023-icwe).

### CLOSER 2023 - Prototype

In this [paper](https://www.iaas.uni-stuttgart.de/publications/Beisel2023_QuantME4VQA.pdf), we extend QuantME to facilitate the modeling of Variational Quantum Algorithms (VQAs) as quantum workflows.
To this end, we introduce QuantME4VQA comprising new task types, data objects, and a comprehensible graphical notation.
Furthermore, we ensure interoperability and portability by extending the QuantME transformation method to enable transforming all new modeling constructs to native modeling constructs of the used workflow language.
To demonstrate its functionality, we implemented a case study solving the Maximum Cut (MaxCut) problem using the Quantum Approximate Optimization Algorithm (QAOA).
The corresponding workflow models and instructions on how to set up the environment and execute the application can be found [here](2023-closer).

### Springer Nature Computer Science 2022 - Prototype

In this [paper](https://link.springer.com/content/pdf/10.1007/s42979-022-01625-9.pdf), we extend our [CLOSER 2022 paper](https://www.iaas.uni-stuttgart.de/publications/Weder2022_QuantumWorkflowRewrite.pdf), analyzing and rewriting quantum workflows to execute them more efficiently using hybrid runtimes, by integrating a provenance approach.
Thus, the use case covers the analysis and rewriting of quantum workflows, while generating a provenance collector in addition to the hybrid programs.
This provenance collector runs in the hybrid runtime and collects provenance data about the quantum computer, the classical hardware, and the running hybrid programs.
The collected provenance data is used to instrument process views that are visualized in the Camunda engine.
Hence, they allow the user to display the modeled and rewritten workflow, which eases monitoring and analysis of quantum workflows.
An example workflow model, as well as detailed instructions on how to set up the required environment and perform the different steps from analysis, over rewriting, to monitoring using process views, can be found [here](2022-sncs).

### Electronics 2022 - Prototype

In this [paper](https://www.mdpi.com/2079-9292/11/19/2983/pdf), we show how to automate the configuration of Readout Error Mitigation (REM) methods using QuantME. 
We analyze the literature for current state-of-the-art REM methods and derive general and method-specific configuration requirements.
To make the error-prone and time-consuming process of configuring REM more efficient, we present an automation approach based on QuantME.
To demonstrate its functionality, we implemented a case study from the quantum humanities domain, performing clustering and classification by means of quantum algorithms.
The corresponding workflow models and instructions on how to set up the environment and execute the application can be found [here](2022-electronics).

### EDOC 2022 - Prototype

We introduce an approach that generates workflow models from existing script-based quantum implementations.
Our approach first splits the script-based implementations into their quantum and classical parts.
These parts are then orchestrated by a generated workflow model that resembles the original execution order of the script and ensures correct data flow between them.
Furthermore, deployment models are generated for each part to enable automated deployment.
An example script-based implementation, as well as detailed instructions on how to set up the required environment and perform the different steps of the approach, can be found [here](2022-edoc).

### CLOSER 2022 - Prototype

In this [paper](https://www.iaas.uni-stuttgart.de/publications/Weder2022_QuantumWorkflowRewrite.pdf), we introduce a method to enable modeling all tasks implementing hybrid quantum algorithms in a workflow model while increasing the efficiency through hybrid runtimes.
Such hybrid runtimes allow the upload of quantum and classical programs together as so-called hybrid programs and optimize their execution.
However, modeling the invocation of hybrid programs directly in the workflow decreases the modularity and understandability, as all tasks implementing the hybrid quantum algorithm are hidden.
Thus, we analyze the workflow model to detect optimization candidates that can benefit from hybrid runtimes, check their suitability based on constraints of the runtimes, generate a corresponding hybrid program, and rewrite the workflow to invoke it.
An example workflow model comprising two optimization candidates, as well as detailed instructions on how to set up the required environment and perform the different steps of the method, can be found [here](2022-closer).

### EDOC 2021 - Prototype

In this [demonstration](https://www.iaas.uni-stuttgart.de/publications/Weder2021_MODULO.pdf), we present the MODULO framework to model, transform, deploy, and execute quantum workflows.
It incorporates a workflow modeling extension for quantum computing (see [Quantum4BPMN](https://github.com/UST-QuAntiL/QuantME-Quantum4BPMN)) with a graphical notation to ease the modeling of quantum workflows.
Additionally, it provides an integrated toolchain supporting the automated transformation of resulting workflow models to native workflow models to retain their portability, as well as the deployment of the quantum workflow with the required services and their binding.
To demonstrate the functionality, we introduce a workflow model implementing Simon's algorithm and discuss all steps, from the modeling of required deployment models, over the modeling of the quantum workflow and its transformation to a native BPMN workflow model, to the deployment of required services, and the workflow execution.
Detailed instructions on how to set up the MODULO framework and perform the different steps can be found [here](2021-edoc).

### ICWS 2021 - Prototype

In this [paper](https://www.iaas.uni-stuttgart.de/publications/Weder2021_OrchestrationsInSuperposition.pdf), we motivate the need for two orchestrations that are required to implement non-trivial hybrid quantum applications:
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

* Beisel, Martin; Barzen, Johanna; Bechtold, Marvin; Leymann, Frank; Truger, Felix; Weder, Benjamin:
  **Metamodel and Formalization to Model, Transform, Deploy, and Execute Quantum Workflows**.
  In: Cloud Computing and Services Science, Springer, 2024

* Beisel, Martin; Gemeinhardt, Felix; Salm, Marie; Weder, Benjamin:
  [**A Practical Introduction for Developing and Operating Hybrid Quantum Applications**](https://link.springer.com/chapter/10.1007/978-3-031-34444-2_36).
  In: Proceedings of the 23rd International Conference on Web Engineering (ICWE 2023), Springer, 2023 

* Beisel, Martin; Barzen, Johanna; Bechtold, Marvin; Leymann, Frank; Truger, Felix; Weder, Benjamin:
  [**QuantME4VQA: Modeling and Executing Variational Quantum Algorithms using Workflows**](https://www.iaas.uni-stuttgart.de/publications/Beisel2023_QuantME4VQA.pdf).
  In: Proceedings of the 13th International Conference on Cloud Computing and Services Science (CLOSER 2023), SciTePress, 2023

* Weder, Benjamin; Barzen, Johanna; Beisel, Martin; Leymann, Frank:
  [**Provenance‑Preserving Analysis and Rewrite of Quantum Workfows for Hybrid Quantum Algorithms**](https://link.springer.com/content/pdf/10.1007/s42979-022-01625-9.pdf).
  In: SN Computer Science. Vol. 4(233), Springer, 2023

* Beisel, Martin; Barzen, Johanna; Leymann, Frank; Truger, Felix; Weder, Benjamin; Yussupov, Vladimir:
  [**Configurable Readout Error Mitigation in Quantum Workflows**](https://www.mdpi.com/2079-9292/11/19/2983/pdf).
  In: Electronics. Vol. 11(19), MDPI, 2022

* Vietz, Daniel; Barzen, Johanna; Leymann, Frank; Weder, Benjamin:
  [**Quantum-Classical Splitting of Scripts for the Generation of Quantum Workflows**](https://link.springer.com/chapter/10.1007/978-3-031-17604-3_15)
  In: Proceedings of the 26th International Enterprise Distributed Object Computing Conference (EDOC 2022), Springer, 2022

* Weder, Benjamin; Barzen, Johanna; Beisel, Martin; Leymann, Frank:
  [**Analysis and Rewrite of Quantum Workflows: Improving the Execution of Hybrid Quantum Algorithms**](https://www.iaas.uni-stuttgart.de/publications/Weder2022_QuantumWorkflowRewrite.pdf).
  In: Proceedings of the 12th International Conference on Cloud Computing and Services Science (CLOSER 2022), SciTePress, 2022

* Weder, Benjamin; Barzen, Johanna; Leymann, Frank:
  [**MODULO: Modeling, Transformation, and Deployment of Quantum Workflows**](https://www.iaas.uni-stuttgart.de/publications/Weder2021_MODULO.pdf).
  In: Proceedings of the 25th International Enterprise Distributed Object Computing Workshop (EDOCW 2021), IEEE, 2021

* Weder, Benjamin; Barzen, Johanna; Leymann, Frank; Zimmermann, Michael:
  [**Hybrid Quantum Applications Need Two Orchestrations in Superposition: A Software Architecture Perspective**](https://www.iaas.uni-stuttgart.de/publications/Weder2021_OrchestrationsInSuperposition.pdf).
  In: Proceedings of the 18th IEEE International Conference on Web Services (ICWS 2021), IEEE, 2021

* Weder, Benjamin; Barzen, Johanna; Leymann, Frank; Salm, Marie:
  [**Automated Quantum Hardware Selection for Quantum Workflows**](https://www.mdpi.com/2079-9292/10/8/984/pdf).
  In: Electronics. Vol. 10(8), MDPI, 2021

* Weder, Benjamin; Breitenbücher, Uwe; Leymann, Frank; Wild, Karoline:
  [**Integrating Quantum Computing into Workflow Modeling and Execution**](https://www.iaas.uni-stuttgart.de/publications/Weder2020_QuantumWorkflows.pdf).
  In: Proceedings of the 13th IEEE/ACM International Conference on Utility and Cloud Computing (UCC 2020), IEEE, 2020

## Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss

Dies ist ein Forschungsprototyp.
Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
