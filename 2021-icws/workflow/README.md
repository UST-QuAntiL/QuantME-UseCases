# Quantum Machine Learning Workflow 

This folder contains a demonstration workflow executing different quantum machine learning algorithms.

### Building the Workflow

1. Run `mvn clean package`  inside this folder.
2. When completed, the built product for the workflow can be found in `target/quantum-workflow.war`

### Deployment of the Workflow to Camunda

After building the workflow, it can be deployed to a [Camunda engine](https://camunda.com/download/) by dropping the WAR file in the `webapps` folder of the corresponding Tomcat server.

The Camunda engine can also be spinned up using the provided [Dockerfile](Dockerfile):

```
docker build -t quantme/qml-workflow
docker run -it -p 8080:8080 quantme/qml-workflow
```

Thereby, the current version of the workflow is automatically deployed to the Camunda engine on startup.
Please use the corresponding environment variables defined in the [Dockerfile](Dockerfile) to configure the endpoints of the related [clustering](../services/clustering) and [classification](../services/classification) services.
