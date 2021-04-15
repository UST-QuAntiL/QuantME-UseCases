#!/bin/bash
# Parameters:
# $VMIP
# $Port


CSARROOT=$(find ~ -maxdepth 1 -path "*.csar");
IFS=';' read -ra FILES <<< "$DAs"
for i in "${FILES[@]}"; do
    IFS=',' read -ra ENTRY <<< "$i"
    if [[ ( -f $CSARROOT${ENTRY[1]} ) && ( ${ENTRY[1]} == *.war ) ]]; then
        cd ~/camunda/server/apache-tomcat-9.0.36/webapps
        # extract properties file
        jar xf $(basename ${ENTRY[1]}) WEB-INF/classes/config.properties
        
        # set IP of camunda engine
        sed -i "/engine/Is/{IP}/$VMIP/" WEB-INF/classes/config.properties
        sed -i "/engine/Is/{PORT}/$Port/" WEB-INF/classes/config.properties

        # update war file        
        jar uf $(basename ${ENTRY[1]}) WEB-INF/classes/config.properties
        
        # clean up       
        rm -r WEB-INF
    fi
done
