FROM planqk/db:v1.0.0
LABEL maintainer = "Benjamin Weder <weder@iaas.uni-stuttgart.de>"

RUN mkdir /temp 
WORKDIR /temp

COPY init-db.sh /docker-entrypoint-initdb.d/init-db.sh
COPY schema.sql schema.sql
COPY data.sql data.sql

CMD su postgres -c "/usr/local/bin/docker-entrypoint.sh postgres"