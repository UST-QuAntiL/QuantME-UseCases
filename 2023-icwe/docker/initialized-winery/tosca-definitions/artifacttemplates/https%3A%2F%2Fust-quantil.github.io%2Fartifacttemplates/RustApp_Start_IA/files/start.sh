#!/bin/bash

sudo apt-get update
sudo apt-get install -yqq unzip

echo "Searching for DA containing Rust application"
IFS=';' read -ra FILES <<< "$DAs"
for i in "${FILES[@]}"; do
    IFS=',' read -ra ENTRY <<< "$i"
    if [[ ( -f $CSARROOT${ENTRY[1]} ) && ( ${ENTRY[1]} == *.zip ) ]]; then
        sudo unzip $CSARROOT${ENTRY[1]} -d ~/app
        break
    fi
done
cd ~/app
echo "Found application comprises the following files:"
ls

echo "Starting application..."
sudo cargo run
