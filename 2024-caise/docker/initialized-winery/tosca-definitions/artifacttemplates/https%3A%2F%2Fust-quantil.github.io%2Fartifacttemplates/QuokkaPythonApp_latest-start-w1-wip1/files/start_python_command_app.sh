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
      # Split the StartupCommand into an array of commands using '&&' as the delimiter
      IFS='&&' read -ra commands <<< "$StartupCommand"

      # Get the last command in the array and inject 'nohup'
      last_command=${commands[-1]}
      nohup_last_command="nohup $last_command"

      # Reconstruct the StartupCommand with 'nohup' injected before the last command
      #new_command=$(IFS='&&' ; echo "${commands[@]:0:${#commands[@]}-1} && $nohup_last_command")
      new_command=""
      for ((i = 0; i < ${#commands[@]} - 1; i++)); do
          new_command+=" ${commands[i]} &&"
      done
      new_command+=" nohup_last_command"

      echo "$new_command" ' > log.log 2>&1 &' >> ~/$Name/startup.sh
  else
      echo 'Starting on specified port: '
      # Split the StartupCommandElse into an array of commands using '&&' as the delimiter
      IFS='&&' read -ra commands_else <<< "$StartupCommand"

      # Get the last command in the array and inject 'nohup'
      last_command_else=${commands_else[-1]}
      nohup_last_command_else="nohup $last_command_else"

      # Reconstruct the StartupCommandElse with 'nohup' injected before the last command
      #new_command_else=$(IFS='&&' ; echo "${commands_else[@]:0:${#commands_else[@]}-1} && $nohup_last_command_else")

      # Reconstruct the StartupCommandElse with 'nohup' injected before the last command
      # Construct the command part with 'nohup' for the last command
      new_command_else=""
      for ((i = 0; i < ${#commands_else[@]} - 1; i++)); do
          new_command_else+=" ${commands_else[i]} &&"
      done
      new_command_else+=" $nohup_last_command_else"

      echo "$new_command_else --port=$vmPort" ' > log.log 2>&1 &' >> ~/$Name/startup.sh
  fi
fi

(cd ~/$Name/ && nohup sh startup.sh &)
echo 'Started'
sleep 5
