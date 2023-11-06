#!/bin/bash

echo 'Name:'$Name
echo 'StartupCommand:'$StartupCommand
if [[ $StartupCommand == nohup* ]]; then
	echo "Starting App using existing startup command..."
	echo $StartupCommand >> ~/$Name/startup.sh
else
	echo "Starting App using modifying using nohup..."
	echo 'nohup ' $StartupCommand  ' > log.log 2>&1 &'  >> ~/$Name/startup.sh
fi


(cd ~/$Name/ && nohup sh startup.sh &)
echo 'Started'
sleep 5



