#!/bin/bash
# Parameters:
# $Port

sed -i "s/8080/$Port/g" ~/camunda/server/apache-tomcat-9.0.36/conf/server.xml

