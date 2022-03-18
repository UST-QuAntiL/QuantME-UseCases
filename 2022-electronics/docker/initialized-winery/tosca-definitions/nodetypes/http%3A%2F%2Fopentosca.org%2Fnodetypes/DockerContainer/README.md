# DockerContainer [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)  

> This node type installs, configures, and starts a Docker container.

## Description:

```xml
<Properties xmlns="http://www.example.org">
 <Port/>
 <ContainerPort/>
 <ContainerID/>
 <ContainerIP/>
 <ImageID/>
 <ContainerMountPath>/etc/openmtc/certs</ContainerMountPath>
 <HostMountFiles>/home/ubuntu/ca-smartorchestra.crt</HostMountFiles>
 <!-- Optional on NodeType inherting from the DockerContainer NodeType-->
 <ENV_EP>get_input: OpenMTCBackend.Endpoint</ENV_EP>
 <ENV_ORIGINATOR_PRE>//smartorchestra.de/backend</ENV_ORIGINATOR_PRE>
 <ENV_SSL_CRT>/etc/openmtc/certs/mqtt-connector.cert.pem</ENV_SSL_CRT>
 <ENV_SSL_KEY>/etc/openmtc/certs/mqtt-connector.key.pem</ENV_SSL_KEY>
 <ENV_BROKER_EP>[get_property: Ubuntu-VM_14.04-w1 VMIP]:8883</ENV_BROKER_EP>
 <ENV_TOPIC_PRE>get_input: Adapter.Topic_Pre</ENV_TOPIC_PRE>
 <ENV_TOPIC_INDEX_LOCATION>1</ENV_TOPIC_INDEX_LOCATION>
 <ENV_TOPIC_INDEX_DEVICE>2</ENV_TOPIC_INDEX_DEVICE>
 <ENV_FIWARE_SERVICE>get_input: FIWARE_Service</ENV_FIWARE_SERVICE>
 <ENV_MQTTS_ENABLED>true</ENV_MQTTS_ENABLED>
 <ENV_MQTTS_CA_CERTS>/etc/openmtc/certs/ca-smartorchestra.crt</ENV_MQTTS_CA_CERTS>
</Properties>
<DeploymentArtifacts xmlns:otateIgeneral="http://opentosca.org/artifacttemplates"
                     xmlns:otatyIgeneral="http://opentosca.org/artifacttypes">
 <DeploymentArtifact name="OpenMTC_MqttConnector_DockerImage_DA"
   artifactType="otatyIgeneral:DockerContainerArtifact"
   artifactRef="otateIversioned:OpenMTC_MqttConnector_DockerImage_AT"/>
 <DeploymentArtifact name="ca-chain.cert_DA" artifactType="otatyIgeneral:DockerVolumeArtifact_1-w1-wip1"
   artifactRef="otateIgeneral:CA-Chain"/>
 <DeploymentArtifact name="Mqtt-Connector.Cert" artifactType="otatyIgeneral:DockerVolumeArtifact_1-w1-wip1"
   artifactRef="otateIgeneral:Mqtt-Connector.Cert_AT"/>
 <DeploymentArtifact name="Mqtt-Connector-Key" artifactType="otatyIgeneral:DockerVolumeArtifact_1-w1-wip1"
   artifactRef="otateIgeneral:Mqtt-Connector-Key"/>
</DeploymentArtifacts>
```

#### Port & ContainerPort

These Properties set the Port on which the container should be exposed, while ContainerPort should be the port on which the DockerContainer exposes its functionality. This is just like e.g. executing ```docker run -p 80:80``` in bash.

#### ContainerID

This property is used to identify containers on a DockerEngine, if you start the container via OpenTOSCA leave this property empty.

#### ContainerIP

This property will contain the IP to connect to the started container. Leave empty when you start the container with OpenTOSCA.

#### ImageID

This property specifies an image id on a docker image repository such as Dockerhub e.g. ubuntu:18.04 would be an acceptable value. If this is set, any attached DeploymentArtifact of the type DockerContainerArtifact or ArchiveArtifact (containing a .zip with Dockerfile and additionally needed files) are ignored.

#### ContainerMountPath & HostMountFiles

This property specifies the location inside a container where a single volume can be mounted. Either files form the local host of the hosting DockerEngine can be added to the volume (e.g. <HostMountFiles>/home/ubuntu/casmartorchestra.crt</HostMountFiles>) or any attached DeploymentArtifact of the type DockerVolumeArtifact_1-w1-wip1 (See example above).

#### ENV_

These Properties (starting with the prefix ENV_) allows NodeType that inherit from the DockerContainer NodeType to specify different environment variables to be passed to the container when starting it (e.g. ```docker run -e SomeVar=val ..```). Additionally, a modeler can reference other properties to set the value of ENV_ properties. E.g. ```[get_property: Ubuntu-VM_14.04-w1 VMIP]:8883``` Would reference the property VMIP of the NodeTemplate Ubuntu-VM_14.04-w1 and concatenate it with the string ```:8883```. Note: This is experimental, currently only simple reference and concatenating it with a string at the end is possible.

## Haftungsausschluss

Dies ist ein Forschungsprototyp und enthält insbesondere Beiträge von Studenten.
Diese Software enthält möglicherweise Fehler und funktioniert möglicherweise, insbesondere bei variierten oder neuen Anwendungsfällen, nicht richtig.
Insbesondere beim Produktiveinsatz muss 1. die Funktionsfähigkeit geprüft und 2. die Einhaltung sämtlicher Lizenzen geprüft werden.
Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden ausgeschlossen.

## Disclaimer of Warranty

Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor
provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT,
MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the
appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of
permissions under this License.
