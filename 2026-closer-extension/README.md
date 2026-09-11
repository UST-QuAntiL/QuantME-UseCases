# Quantum Low-Code Modeling and Execution Platform

This repository contains the open-source prototype and evaluation artifacts for the paper:

> **Low-Code Quantum Application Development: From Modeling to Workflow Execution**

The prototype provides a low-code environment for modeling and executing hybrid quantum-classical applications. It allows users to describe quantum applications using graphical, high-level abstractions instead of implementing the complete algorithm directly in a quantum SDK.

The platform supports the complete development process, from problem description and algorithm recommendation to model instantiation, model adaptation, transformation, deployment, and execution.

Two use cases are provided:

1. **Combinatorial optimization with QAOA**, using a MaxCut problem.
2. **Quantum clustering with QHAna**, demonstrating the integration of quantum machine-learning functionality into hybrid workflows.

The repository also contains the raw data used for the runtime analysis and user study reported in the paper.

---

## Repository Contents

The repository contains the following artifacts:

* **Raw data of the user study**
  [user-study](https://github.com/UST-QuAntiL/QuantME-UseCases/blob/feature/2026-closer-extension/user-study)

* **Use-case documentation**

* **Docker-based Setup**

---

# Modeling Language

The Quantum Low-Code Modeling Language combines classical and quantum concepts and supports different levels of abstraction, ranging from individual quantum gates to complete algorithm blocks.

## Data Types

### Classical Data Types

| Block               | Properties | Description                                            |
| ------------------- | ---------- | ------------------------------------------------------ |
| **Binary Type**     | `value`    | Bit or Boolean value.                                  |
| **Numeric Type**    | `value`    | Integer or floating-point value.                       |
| **Physical Type**   | `value`    | Physical quantities such as duration or angle.         |
| **Collection Type** | `value`    | A collection of values, potentially of varying length. |

### Quantum Data Types

| Block       | Properties | Description                                            |
| ----------- | ---------- | ------------------------------------------------------ |
| **Qubit**   | `value`    | Basic unit of quantum information.                     |

---

## Boundary Elements

Boundary elements represent operations at the interface between classical and quantum computation.

| Block            | Properties                           | Description                                                                                                                    |
| ---------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **EncodeValue**  | `encodingType`, `bound`              | Encodes a classical value into a quantum state. Supported encoding types include basis, angle, amplitude, and matrix encoding. |
| **PrepareState** | `quantumStateName`                   | Prepares a predefined quantum state, such as a Bell, GHZ, or W state.                                                          |
| **Measurement**  | `measurementBasis`, `qubitSelection` | Measures selected qubits and produces classical output.                                                                        |

---

## Operators

| Block                   | Properties                                                               | Description                                                                       |
| ----------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **ArithmeticOperation** | `operation`                                                              | Performs arithmetic operations such as addition, subtraction, and multiplication. |
| **BitwiseOperation**    | `operation`                                                              | Performs bitwise operations such as AND, OR, XOR, and NOT.                        |
| **ComparisonOperation** | `operation`                                                              | Compares values using equality, inequality, and ordering operations.              |
| **MinMax**              | `operation`                                                              | Selects the minimum or maximum of multiple values.                                |
| **OracleElement**       | oracle configuration                                                     | Represents an oracle used by algorithms such as search procedures.                |
| **CustomNode**          | `classicalInputs`, `quantumInputs`, `classicalOutputs`, `quantumOutputs` | User-defined operation with custom classical and quantum interfaces.              |

---

## Control Flow

The modeling language supports classical control flow within hybrid quantum-classical applications.

| Block     | Properties  | Description                                              |
| --------- | ----------- | -------------------------------------------------------- |
| **If**    | `condition` | Executes a block conditionally based on a Boolean input. |
| **While** | `condition` | Repeats a block while a condition is true.               |

These constructs allow classical measurement results and other values to influence subsequent quantum or classical operations.

---

## Circuit Primitives

Circuit primitives allow users to specify quantum circuits directly when a lower level of abstraction is required.

| Block             | Properties      | Description                                                     |
| ----------------- | --------------- | --------------------------------------------------------------- |
| **Qubit Circuit** | —               | Represents a quantum register or circuit-level qubit structure. |
| **H**             | —               | Hadamard gate.                                                  |
| **RX(θ)**         | `parameterType` | Rotation around the X-axis.                                     |
| **RY(θ)**         | `parameterType` | Rotation around the Y-axis.                                     |
| **RZ(θ)**         | `parameterType` | Rotation around the Z-axis.                                     |
| **T**             | —               | T gate.                                                         |
| **X**             | —               | Pauli-X gate.                                                   |
| **Y**             | —               | Pauli-Y gate.                                                   |
| **Z**             | —               | Pauli-Z gate.                                                   |
| **S**             | —               | S gate.                                                         |
| **SX**            | —               | Square-root of X gate.                                          |
| **SDG**           | —               | Inverse S gate.                                                 |
| **TDG**           | —               | Inverse T gate.                                                 |
| **CNOT**          | —               | Controlled-X gate.                                              |
| **SWAP**          | —               | Swaps the states of two qubits.                                 |
| **CY**            | —               | Controlled-Y gate.                                              |
| **CZ**            | —               | Controlled-Z gate.                                              |
| **CH**            | —               | Controlled-Hadamard gate.                                       |
| **CRX(θ)**        | `parameterType` | Controlled rotation around the X-axis.                          |
| **CRY(θ)**        | `parameterType` | Controlled rotation around the Y-axis.                          |
| **CRZ(θ)**        | `parameterType` | Controlled rotation around the Z-axis.                          |
| **Toffoli**       | —               | Controlled-controlled-X gate.                                   |
| **CSWAP**         | —               | Controlled SWAP gate.                                           |
| **Splitter**      | `output-count`  | Splits a quantum register into individual qubits.               |
| **Merger**        | `input-count`   | Combines multiple qubits into a quantum register.               |

---

## Algorithm Blocks

The platform additionally provides higher-level algorithm blocks that encapsulate established quantum algorithms and quantum machine-learning procedures.

Examples include:

* Quantum Approximate Optimization Algorithm (QAOA)
* Quantum Fourier Transform (QFT)
* Grover's Search
* Variational Quantum Eigensolver (VQE)
* Quantum classification
* Quantum clustering

Algorithm blocks expose only the parameters relevant to their configuration while hiding their underlying circuit-level implementation.

This allows beginners to work with established algorithms without manually constructing their circuits, while experienced users can still inspect and adapt the resulting models.

---

# Templates

The platform provides reusable templates for common quantum algorithms and recurring computational structures.

Available templates include:

* QAOA 
* Quantum clustering
* Quantum classification
* SWAP Test
* Hadamard Test

Templates provide a complete starting model that users can adapt to their specific problem.

Users can also save their own low-code models as templates, allowing the template library to be extended with domain-specific or project-specific algorithms.

---

# Modeling and Execution Process

The platform supports the following development process:

```text
Problem Definition
        ↓
Algorithm Identification
        ↓
Algorithm Selection
        ↓
Model Instantiation
        ↓
Model Adaptation
        ↓
Model Enrichment
        ↓
Model Transformation
        ↓
Service Deployment
        ↓
Workflow Execution
```

## 1. Problem Definition

Users can describe the problem they want to solve using natural language.

For example:

```text
I have five locations connected by roads. I want to split the locations
into two groups so that as many roads as possible go between the groups.
```

Users who already know which algorithm they want to use can skip this step and directly select an existing algorithm or template.

## 2. Algorithm Identification

The platform uses an LLM-based recommendation component to identify potentially suitable quantum algorithms based on the problem description.

The recommendation process is grounded in the quantum computing pattern language stored in the Pattern Atlas.

## 3. Algorithm Selection

Candidate algorithms are presented to the user together with information about the corresponding quantum computing patterns.

The user can inspect the recommended algorithms and select the one that best matches the problem.

## 4. Model Instantiation

The selected algorithm template is loaded into the low-code modeler.

The resulting model already contains the general structure of the selected algorithm.

## 5. Model Adaptation

Users can adapt the generated model by:

* configuring algorithm parameters,
* replacing or adding operations,
* specifying problem-specific values,
* adding classical logic,
* modifying quantum operations, and
* defining resource constraints.

The modeler continuously validates the model during editing.

## 6. Model Enrichment

The low-code backend resolves implementations for model elements that do not yet contain an executable implementation.

Implementations can originate from the Pattern Atlas or connected services such as QHAna.

## 7. Model Transformation

The enriched model can be transformed into an executable artifact.

Depending on the model, the platform generates either:

* an OpenQASM program, or
* a hybrid quantum-classical workflow.

Hybrid workflows represent quantum operations using QuantME elements and classical operations using corresponding workflow service tasks.

The resulting workflow is transformed into a BPMN-compliant executable workflow.

## 8. Service Deployment and Execution

The generated workflow and its associated services are deployed to the execution environment.

The workflow engine coordinates classical and quantum tasks and handles their data and control dependencies.

Quantum tasks can be executed on available quantum computers or simulators through the integrated quantum execution infrastructure.

---

# Architecture

The prototype integrates the following components:

* **Quantum Low-Code Modeler** – graphical modeling and user interaction
* **Low-Code Backend** – model enrichment and transformation
* **Pattern Atlas** – quantum computing patterns and reusable templates
* **QHAna** – quantum and classical machine-learning plugins
* **QuantME** – representation of quantum workflow tasks
* **OpenTOSCA Ecosystem** – deployment of generated services
* **NISQ Analyzer** – analysis and selection of suitable quantum hardware
* **QProv** – quantum resource and provenance information
* **Qunicorn** – unified interface for quantum execution
* **Workflow Engine** – orchestration of hybrid quantum-classical workflows

---

# Use Cases

## 1. Combinatorial Optimization with QAOA

The first use case demonstrates how a user without prior quantum programming expertise can solve a MaxCut problem.

The user describes the problem as:

```text
I have five locations connected by roads. I want to split the locations
into two groups so that as many roads as possible go between the groups.
```

The platform identifies QAOA as a suitable algorithm and provides the corresponding QAOA template.

The resulting model can be adapted and transformed into a hybrid workflow.

The workflow contains the classical optimization loop required by QAOA and executes the quantum circuit on a suitable quantum backend.

For the example provided with this repository, the resulting objective function value is:

```text
5
```

---

## 2. Quantum Clustering with QHAna

The second use case demonstrates the integration of quantum machine-learning functionality.

The example problem is:

```text
I have a dataset of costume images and want to group similar costumes
together to see whether patterns emerge across films.
```

The platform identifies clustering as the relevant task and provides a clustering template.

The user configures:

* the input dataset,
* the desired number of clusters, and
* the selected classical or quantum backend.

During model enrichment, the clustering operation is resolved through QHAna.

The resulting workflow invokes the corresponding QHAna plugins as service tasks, allowing the machine-learning operation to be executed as part of the same hybrid workflow.

---

# Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss

Dies ist ein Forschungsprototyp. Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
