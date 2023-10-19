#!/bin/bash

echo 'Name:'$Name
echo 'StartupCommand:'$StartupCommand
echo $StartupCommand >> ~/$Name/startup.sh
(cd ~/$Name/ && nohup sh startup.sh &)
sleep 5
exit 1


