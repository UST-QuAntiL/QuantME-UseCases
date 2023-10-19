#!/bin/bash

echo 'Name:'$Name

sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip -qq
	
pip3 install --upgrade pip

sudo mkdir -p ~/$Name

#find csar root
csarRoot=$(find ~/.. -maxdepth 1 -path "*.csar");

IFS=';' read -ra NAMES <<< "$DAs";
for i in "${NAMES[@]}"; do
	echo "KeyValue-Pair: "
    	echo $i
	IFS=',' read -ra OT_PATH <<< "$i";    
	echo "Key: "
    	echo ${OT_PATH[0]}
    	echo "Value: "
    	echo ${OT_PATH[1]}
	if [[ "${OT_PATH[1]}" == *.tar.gz ]]; then
		echo "Extracting Python Service..."
		sudo tar -xf $csarRoot${OT_PATH[1]} -C ~/$Name
		echo "Installing dependencies..."
		pip install --no-cache-dir -r ~/$Name/requirements.txt
	fi
	if [[ "${OT_PATH[1]}" == *requirements.txt ]]; then
		echo "Installing dependencies..."
		pip install --no-cache-dir -r $csarRoot${OT_PATH[1]}
	fi
	if [[ "${OT_PATH[1]}" == *.py ]]; then
		echo "Copying files..."
		sudo cp $csarRoot${OT_PATH[1]} ~/$Name/$(basename ${OT_PATH[1]})
	fi
done




