#!/bin/bash

echo 'Port:'$Port
echo 'Name:'$Name

cd $Name
nohup python3 -u app.py $Port >app.log 2>&1 </dev/null &
sleep 5
exit 1