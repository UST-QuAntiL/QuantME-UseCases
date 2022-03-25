FROM openjdk:8
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

ARG CAMUNDA_VERSION=7.14

# install the Camunda engine
RUN curl -LO https://downloads.camunda.cloud/release/camunda-bpm/run/$CAMUNDA_VERSION/camunda-bpm-run-$CAMUNDA_VERSION.0.tar.gz \
    && tar xzvf camunda-bpm-run-$CAMUNDA_VERSION.0.tar.gz \
    && rm camunda-bpm-run-$CAMUNDA_VERSION.0.tar.gz

# download history extensions
RUN mkdir -p META-INF/resources/webjars/camunda/app/cockpit/scripts/ \
    && curl -L https://raw.githubusercontent.com/datakurre/camunda-cockpit-plugins/c9741bcceac99d392997de36553f8037f33f031c/definition-historic-activities.js -o META-INF/resources/webjars/camunda/app/cockpit/scripts/definition-historic-activities.js \
    && curl -L https://raw.githubusercontent.com/datakurre/camunda-cockpit-plugins/c9741bcceac99d392997de36553f8037f33f031c/instance-historic-activities.js -o META-INF/resources/webjars/camunda/app/cockpit/scripts/instance-historic-activities.js \
    && curl -L https://raw.githubusercontent.com/datakurre/camunda-cockpit-plugins/c9741bcceac99d392997de36553f8037f33f031c/instance-route-history.js -o META-INF/resources/webjars/camunda/app/cockpit/scripts/instance-route-history.js \
    && curl -L https://raw.githubusercontent.com/datakurre/camunda-cockpit-plugins/c9741bcceac99d392997de36553f8037f33f031c/config.js -o META-INF/resources/webjars/camunda/app/cockpit/scripts/config.js

# update JAR with history extension
RUN jar uf internal/webapps/camunda-webapp-webjar-$CAMUNDA_VERSION.0.jar META-INF

EXPOSE 8080

CMD bash start.sh
