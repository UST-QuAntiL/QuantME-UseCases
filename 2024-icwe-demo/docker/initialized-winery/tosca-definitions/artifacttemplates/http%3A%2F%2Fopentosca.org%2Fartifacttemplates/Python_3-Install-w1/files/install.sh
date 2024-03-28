#!/bin/sh
sudo apt-get update -qq;
sudo DEBIAN_FRONTEND=noninteractive TZ="UTC" apt-get install -y -qq python3 python3-pip;
