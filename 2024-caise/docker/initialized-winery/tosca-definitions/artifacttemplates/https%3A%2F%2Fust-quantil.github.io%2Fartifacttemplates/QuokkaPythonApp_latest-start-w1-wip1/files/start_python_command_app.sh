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
        IFS='&&' read -ra commands <<< "$StartupCommand"

        last_command=${commands[-1]}
        nohup_last_command="nohup $last_command"

        new_command=""
        for ((i = 0; i < ${#commands[@]} - 1; i++)); do
            new_command+=" ${commands[i]} &&"
        done
        new_command+=" $nohup_last_command"

        # Remove any leading/trailing spaces
        new_command=${new_command//+( )/ }

        echo "$new_command" ' > log.log 2>&1 &' >> ~/$Name/startup.sh
    else
        echo 'Starting on specified port: '
        IFS='&&' read -ra commands_else <<< "$StartupCommand"

        last_command_else=${commands_else[-1]}
        nohup_last_command_else="nohup $last_command_else"

        new_command_else=""
        for ((i = 0; i < ${#commands_else[@]} - 1; i++)); do
            new_command_else+=" ${commands_else[i]} &&"
        done
        new_command_else+=" $nohup_last_command_else"

        # Remove any leading/trailing spaces
        new_command_else=${new_command_else//+( )/ }

        echo "$new_command_else --port=$vmPort" ' > log.log 2>&1 &' >> ~/$Name/startup.sh
    fi
fi

(cd ~/$Name/ && nohup sh startup.sh &)
echo 'Started'
sleep 5
