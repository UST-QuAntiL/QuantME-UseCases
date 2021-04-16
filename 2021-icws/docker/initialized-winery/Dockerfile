FROM maven:3-jdk-8 as builder
COPY . /temp
WORKDIR /temp

# bundle the different required DAs from the source files
RUN tar -czf data-preparation.tar.gz --directory=/temp/services/data-preparation .
RUN tar -czf clustering.tar.gz --directory=/temp/services/clustering .
RUN tar -czf classification.tar.gz --directory=/temp/services/classification .


FROM opentosca/winery:v3.0.0-M1
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

ENV WINERY_REPOSITORY_PATH /var/repository/hardware-selection

# copy tosca definitions folder to use it as Winery repository
COPY --chown=winery ./tosca-definitions /var/repository/hardware-selection

# add the data preparation service packaged in the builder as DA
COPY --from=builder --chown=winery /temp/data-preparation.tar.gz /var/repository/hardware-selection/artifacttemplates/http%3A%2F%2Fopentosca.org%2Fartifacttemplates/DataPreparation_PythonService_DA/files/data-preparation.tar.gz

# add the clustering service packaged in the builder as DA
COPY --from=builder --chown=winery /temp/clustering.tar.gz /var/repository/hardware-selection/artifacttemplates/http%3A%2F%2Fopentosca.org%2Fartifacttemplates/Clustering_QiskitService_DA/files/clustering.tar.gz

# add the classification service packaged in the builder as DA
COPY --from=builder --chown=winery /temp/classification.tar.gz /var/repository/hardware-selection/artifacttemplates/http%3A%2F%2Fopentosca.org%2Fartifacttemplates/Classification_QiskitService_DA/files/classification.tar.gz