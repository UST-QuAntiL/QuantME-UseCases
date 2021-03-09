FROM openjdk:8
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

ARG CAMUNDA_VERSION=7.14
ARG DOCKERIZE_VERSION=v0.6.1

ENV APACHE_TOMCAT_VERSION "9.0.36"

RUN mkdir /camunda 
WORKDIR /camunda

# install the Camunda engine
RUN wget https://downloads.camunda.cloud/release/camunda-bpm/tomcat/$CAMUNDA_VERSION/camunda-bpm-tomcat-$CAMUNDA_VERSION.0.tar.gz \
    && tar xf camunda-bpm-tomcat-7.14.0.tar.gz -C . \
    && rm camunda-bpm-tomcat-$CAMUNDA_VERSION.0.tar.gz

# clean demo workflow
RUN rm -rf server/apache-tomcat-$APACHE_TOMCAT_VERSION/webapps/camunda-invoice

EXPOSE 8080

CMD server/apache-tomcat-$APACHE_TOMCAT_VERSION/bin/catalina.sh run
