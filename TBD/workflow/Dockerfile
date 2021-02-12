FROM maven:3.6.3-jdk-14 as builder

COPY . /tmp/quantum-workflow
WORKDIR /tmp/quantum-workflow

RUN mvn package -DskipTests

FROM openjdk:8
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

ARG CAMUNDA_VERSION=7.14
ARG DOCKERIZE_VERSION=v0.6.1

ENV APACHE_TOMCAT_VERSION "9.0.36"

ENV ENGINE_IP localhost
ENV ENGINE_PORT 8080
ENV CLUSTERING_IP localhost
ENV CLUSTERING_PORT 8081
ENV CLASSIFICATION_IP localhost
ENV CLASSIFICATION_PORT 8082

RUN mkdir /camunda 

WORKDIR /camunda

# install the Camunda engine
RUN wget https://downloads.camunda.cloud/release/camunda-bpm/tomcat/$CAMUNDA_VERSION/camunda-bpm-tomcat-$CAMUNDA_VERSION.0.tar.gz \
    && tar xf camunda-bpm-tomcat-7.14.0.tar.gz -C . \
    && rm camunda-bpm-tomcat-$CAMUNDA_VERSION.0.tar.gz

# install Dockerize
RUN rm /dev/random && ln -s /dev/urandom /dev/random \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# clean demo workflow
RUN rm -rf server/apache-tomcat-$APACHE_TOMCAT_VERSION/webapps/camunda-invoice

# add quantum workflow example
COPY --from=builder /tmp/quantum-workflow/target/quantum-workflow.war tmp/quantum-workflow.war

RUN unzip -qq tmp/quantum-workflow.war -d server/apache-tomcat-$APACHE_TOMCAT_VERSION/webapps/quantum-workflow \
    && rm tmp/quantum-workflow.war

# load config template
ADD .docker/config.properties.tpl config.properties.tpl

EXPOSE 8080

CMD ls && dockerize -template config.properties.tpl:server/apache-tomcat-$APACHE_TOMCAT_VERSION/webapps/quantum-workflow/WEB-INF/classes/config.properties \
    && server/apache-tomcat-$APACHE_TOMCAT_VERSION/bin/catalina.sh run
