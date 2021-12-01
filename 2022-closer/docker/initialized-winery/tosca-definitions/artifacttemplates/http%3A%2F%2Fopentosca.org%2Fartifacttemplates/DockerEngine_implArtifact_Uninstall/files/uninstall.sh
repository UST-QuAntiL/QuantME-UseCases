#!/bin/bash

sudo apt-get -y remove --auto-remove docker docker-ce #Removes docker and dependencies
sudo rm -rf /var/lib/docker #Removes all data
