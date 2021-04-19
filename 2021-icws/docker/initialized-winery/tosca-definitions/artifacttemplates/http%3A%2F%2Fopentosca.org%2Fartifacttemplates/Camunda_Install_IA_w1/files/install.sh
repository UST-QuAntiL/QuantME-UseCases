#! /bin/bash

wget https://downloads.camunda.cloud/release/camunda-bpm/tomcat/7.14/camunda-bpm-tomcat-7.14.0.tar.gz >> ~/camunda_install.log
sudo mkdir camunda >> ~/camunda_install.log
sudo tar xf camunda-bpm-tomcat-7.14.0.tar.gz -C camunda >> ~/camunda_install.log
sudo chmod -R 777 camunda >> ~/camunda_install.log

# remove example workflows from the engine
sudo rm -rf ~/camunda/server/apache-tomcat-9.0.36/webapps/camunda-invoice
sudo rm -rf ~/camunda/server/apache-tomcat-9.0.36/webapps/camunda-welcome
