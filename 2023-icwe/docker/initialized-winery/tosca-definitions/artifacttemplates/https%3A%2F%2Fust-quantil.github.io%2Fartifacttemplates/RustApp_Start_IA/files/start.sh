#!/bin/bash

sudo apt-get update
sudo apt-get install -yqq unzip

echo "Searching for DA containing Rust application"
echo "DA string: $DAs"
CSARROOT=$(find . -maxdepth 1 -path "*.csar");
echo "CSAR root: $CSARROOT"
IFS=';' read -ra FILES <<< "$DAs"
for i in "${FILES[@]}"; do
    IFS=',' read -ra ENTRY <<< "$i"
    echo "Found DA path: $ENTRY[1]"
    if [[ ( -f $CSARROOT${ENTRY[1]} ) && ( ${ENTRY[1]} == *.zip ) ]]; then
        echo "Found DA to unzip: $CSARROOT${ENTRY[1]}"
        sudo unzip $CSARROOT${ENTRY[1]} -d ~/app
        break
    fi
done
cd ~/app
echo "Found application comprises the following files:"
ls

echo "Starting application $AppName on port $Port..."
sudo PORT=$Port nohup ./$AppName > log.txt 2>&1 </dev/null &
sleep 5
echo "Successfully started application $AppName"
