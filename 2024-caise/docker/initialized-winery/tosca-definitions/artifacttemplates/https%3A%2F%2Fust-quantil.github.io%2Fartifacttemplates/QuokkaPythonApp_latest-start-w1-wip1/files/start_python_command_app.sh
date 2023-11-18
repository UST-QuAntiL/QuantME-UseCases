#!/bin/bash

echo 'Name: '$Name
echo 'StartupCommand: '$StartupCommand
echo 'Port: '$VMOpenPorts
vmPort="${VMOpenPorts%%,*}"

if [[ $StartupCommand == nohup* ]]; then
	echo "Starting App using existing startup command..."
	if [[ -z "${vmPort}" ]]; then
		echo 'Starting on default port...'
		echo $StartupCommand >> ~/$Name/startup.sh
	else
		echo 'Starting on specified port: '
		echo $StartupCommand ' --port=' $vmPort >> ~/$Name/startup.sh
	fi
	echo $StartupCommand >> ~/$Name/startup.sh
else
	echo "Starting App using modifying using nohup..."
	if [[ -z "${vmPort}" ]]; then
		echo 'Starting on default port...'
		echo 'nohup ' $StartupCommand ' > log.log 2>&1 &'  >> ~/$Name/startup.sh
	else
		echo 'Starting on specified port: '
		echo 'nohup ' $StartupCommand ' --port=' $vmPort ' > log.log 2>&1 &'  >> ~/$Name/startup.sh
	fi
fi

(cd ~/$Name/ && nohup sh startup.sh &)
echo 'Started'
sleep 5
