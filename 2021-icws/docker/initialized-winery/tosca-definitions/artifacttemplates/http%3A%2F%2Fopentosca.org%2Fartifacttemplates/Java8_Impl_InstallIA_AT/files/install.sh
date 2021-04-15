#!/bin/bash
sudo add-apt-repository -y ppa:openjdk-r/ppa
sudo apt-get -qy update
sudo apt-get -qy install openjdk-8-jdk openjdk-8-jre
sudo update-alternatives --config java
sudo update-alternatives --config javac
sleep 5
