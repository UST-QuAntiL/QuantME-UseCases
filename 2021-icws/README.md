# ICWS 2021 Prototype

TODO

## Setting up the Hybrid Quantum-Classical Environment

First, we will discuss the steps required to set up the different components realizing the hybrid quantum-clssical modeling and runtime environment.
Thereby, all components except the workflow modeling tool (see [Camunda Modeler](https://camunda.com/download/modeler/)) are available via Docker.
However, in this demonstration, we assume that the workflow was already modeled, and thus, it is accessible in [this folder](./docker/initialized-winery/workflow).
Therefore, all required components can be started using the Docker-Compose file available [here](./docker):

1. Update the [.env](./docker/.env) file with your settings: 
  * ``PUBLIC_HOSTNAME``: Enter the hostname/IP address of your Docker engine. Do *not* use ``localhost``.

2. Run the Docker-Compose file:
```
docker-compose pull
docker-compose up --build
```

3. Wait until all containers are up and running. This may take some minutes.

## Modeling Hybrid Quantum Applications

TODO

## Provisioing the Execution Environment

TODO

## Execution of the Hybrid Quantum Application

TODO

## Troubleshooting

TODO
