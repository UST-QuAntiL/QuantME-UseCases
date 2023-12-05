# Views

The following sections provided detailed information about the quantum, deployment, pattern, and provenance graph views.

## Quantum View

The quantum view utilizes several data source to visualize quantum-specific details.
Device-specific information, such as a quantum devices error rates are retrieved via a provenance system.
Instance-specific information, e.g., the generated circuit, are retrieved from instance data.


| Name                    | Description                                                   | Context                                                       | Representation      | Data Source       |
|-------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------|-------------------|
| circuitVisualization    | graphical representation of the generated circuit             | quantum-circuit-loading task                                  | overlay (graphical) | instance data     |
| circuitDepth            | depth the generated circuit                                  | quantum-circuit-loading task                                  | overlay (graphical) | instance data     |
| circuitWidth            | number of qubits required by the generated circuit            | quantum-circuit-loading task                                  | overlay (graphical) | instance data     |
| qpuName                 | name of the quantum device                                    | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)   | provenance system |
| queueSize               | queue size of the quantum device                              | quantum-circuit-execution task, readout-error-mitigation task | overlay (textual)              | provenance system            |
| numberOfQubits          | number of qubits provided by the quantum device               | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| avgT1Time               | average T1 time of the quantum device's qubits                | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| avgT2Time               | average T2 time of the quantum device's qubits                | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| avgReadoutError         | average readout error of the quantum device's qubits          | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| avgSingleQubitGateError | average single qubit gate error of the quantum device's qubits | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| avgMultiQubitGateError  | average multi qubit gate error of the quantum device's qubits | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| avgSingleQubitGateTime  | average single qubit gate time of the quantum device's qubits | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| avgMultiQubitGateTime   | average multi qubit gate time of the quantum device's qubits  | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| maxGateTime             | maximum gate time of all qubits of the quantum device         | quantum-circuit-execution task, readout-error-mitigation task                                | overlay (textual)              | provenance system            |
| name                    | Inhalt                                                        | Inhalt                                                        | Inhalt              | Inhalt            |
| name                    | Inhalt                                                        | Inhalt                                                        | Inhalt              | Inhalt            |


 avgMultiQubitGateError, avgSingleQubitGateTime, avgMultiQubitGateTime, maxGateTime
## Deployment View

## Pattern View

## Provenance Graph View

