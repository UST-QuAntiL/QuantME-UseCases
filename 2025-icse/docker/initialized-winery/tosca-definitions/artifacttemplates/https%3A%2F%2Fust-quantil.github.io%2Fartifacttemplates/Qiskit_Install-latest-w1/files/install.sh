#!/bin/bash

sudo apt-get update -qq

sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip -qq

pip3 install --upgrade pip

pip install qiskit==0.44.1
