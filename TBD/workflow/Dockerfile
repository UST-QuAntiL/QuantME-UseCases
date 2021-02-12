FROM maven:3.6.3-jdk-14 as builder
COPY . /tmp/quantum-workflow
WORKDIR /tmp/quantum-workflow
RUN mvn package -DskipTests

FROM camunda/camunda-bpm-platform:latest
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

# clean demo workflow
RUN cd /camunda/webapps/ && rm -rf camunda-invoice

# add quantum workflow example
COPY --from=builder /tmp/quantum-workflow/target/quantum-workflow.war /camunda/webapps/
