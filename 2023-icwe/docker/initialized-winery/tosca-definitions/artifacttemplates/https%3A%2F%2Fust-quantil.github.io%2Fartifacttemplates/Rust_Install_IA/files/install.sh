#!/bin/bash

sudo apt-get update >/dev/null
sudo apt-get install -yqq curl >/dev/null
echo "Installing Rust..."
curl https://sh.rustup.rs -sSf -o rust_install.sh
sudo chmod +x rust_install.sh
sudo ./rust_install.sh -y >> ./rust_install.log
echo "Rust successfully installed"
