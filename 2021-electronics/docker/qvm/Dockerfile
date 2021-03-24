FROM ubuntu:18.04
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

WORKDIR temp

RUN apt-get update && apt-get install -yqq wget tar

RUN wget http://downloads.rigetti.com/qcs-sdk/forest-sdk-2.23.0-linux-deb.tar.bz2 \
    && tar -xf forest-sdk-2.23.0-linux-deb.tar.bz2 

RUN yes | forest-sdk-2.23.0-linux-deb/forest-sdk-2.23.0-linux-deb.run

EXPOSE 5666

CMD qvm -S -p 5666