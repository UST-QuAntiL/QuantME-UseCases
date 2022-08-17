FROM maven:3-openjdk-8 as builder

RUN apt-get update -qq && apt-get install -y git

# retrieve sources for v1.0.0 of the process view plugin and build it
RUN git clone -b v1.0.0 https://github.com/UST-QuAntiL/camunda-process-views-plugin.git

RUN mvn clean install -f camunda-process-views-plugin/pom.xml


FROM openjdk:8
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

ARG CAMUNDA_VERSION=7.17
ARG DOCKERIZE_VERSION=v0.6.1

ENV APACHE_TOMCAT_VERSION "9.0.58"

RUN mkdir /camunda 
WORKDIR /camunda

# install the Camunda engine
RUN wget https://downloads.camunda.cloud/release/camunda-bpm/tomcat/$CAMUNDA_VERSION/camunda-bpm-tomcat-$CAMUNDA_VERSION.0.tar.gz \
    && tar xf camunda-bpm-tomcat-7.17.0.tar.gz -C . \
    && rm camunda-bpm-tomcat-$CAMUNDA_VERSION.0.tar.gz

# clean demo workflow
RUN rm -rf server/apache-tomcat-$APACHE_TOMCAT_VERSION/webapps/camunda-invoice

# get build product for the process view plugin
COPY --from=builder camunda-process-views-plugin/target/camunda-process-views-plugin-1.0-SNAPSHOT.jar /camunda/camunda-process-views-plugin-1.0-SNAPSHOT.jar

# move plugin to camunda lib folder
RUN mv /camunda/camunda-process-views-plugin-1.0-SNAPSHOT.jar server/apache-tomcat-$APACHE_TOMCAT_VERSION/webapps/camunda/WEB-INF/lib

EXPOSE 8080

CMD server/apache-tomcat-$APACHE_TOMCAT_VERSION/bin/catalina.sh run
