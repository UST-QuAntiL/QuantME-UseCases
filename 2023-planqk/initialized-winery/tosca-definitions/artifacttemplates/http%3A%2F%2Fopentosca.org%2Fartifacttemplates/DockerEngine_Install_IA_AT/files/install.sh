#!/bin/bash

installed=$(dpkg -s docker-ce| grep installed)

if [ "" != "$installed" ]; then
	echo "Docker Engine already installed";
	exit 0;
else
	echo "Installing Docker Engine";
	export DEBIAN_FRONTEND=noninteractive;
	sudo dpkg --configure -a;
	curl -sSL https://get.docker.com | sh
	sudo sed -ie "s@ExecStart=\/usr\/bin\/dockerd -H fd:\/\/@ExecStart=\/usr\/bin\/dockerd -H fd:\/\/ -H tcp:\/\/0.0.0.0:2375 -H unix:///var/run/docker.sock@g" /lib/systemd/system/docker.service
	echo 'DOCKER_OPTS="-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock"' >> /etc/default/docker
	sudo systemctl daemon-reload
	sudo service docker restart
	sudo usermod -aG docker $USER
	exit 0;
fi
exit 0;

#sudo sh -c "echo '127.0.0.1' $(hostname) >> /etc/hosts";
#sudo apt-get update
#sudo apt-get -y -q install apt-transport-https ca-certificates
#sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
#sudo echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
#sudo apt-get update
#sudo apt-get -y -q install linux-image-extra-$(uname -r) linux-image-extra-virtual
#sudo apt-get -y -q install docker-engine
#sudo echo 'DOCKER_OPTS="-D -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock"' > /etc/default/docker
#sudo service docker restart
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#sudo apt-get update
#sudo apt-get install -y docker-ce
#sudo service docker stop
#sudo groupadd docker
#sudo usermod -aG docker $USER
#sudo sed -ie "s/ExecStart=\/usr\/bin\/dockerd -H fd:\/\/$/ExecStart=\/usr\/bin\/dockerd -H fd:\/\/ -H tcp:\/\/0.0.0.0:2375 -H unix:///var/run/docker.sock/g" /lib/systemd/system/docker.service
#sudo echo 'DOCKER_OPTS="-D -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock"' > /etc/default/docker
#sudo service docker restart
