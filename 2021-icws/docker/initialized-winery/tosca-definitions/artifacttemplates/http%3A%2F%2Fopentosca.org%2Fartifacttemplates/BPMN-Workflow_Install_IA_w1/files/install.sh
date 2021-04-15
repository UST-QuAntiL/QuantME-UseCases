#!/bin/bash
CSARROOT=$(find ~ -maxdepth 1 -path "*.csar");
IFS=';' read -ra FILES <<< "$DAs"
for i in "${FILES[@]}"; do
    IFS=',' read -ra ENTRY <<< "$i"
    if [[ ( -f $CSARROOT${ENTRY[1]} ) && ( ${ENTRY[1]} == *.war ) ]]; then
        sudo cp $CSARROOT${ENTRY[1]} ~/camunda/server/apache-tomcat-9.0.36/webapps
    fi
done
sleep 30
