#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
sudo update-locale LANG=en_US.UTF-8 LANGUAGE=en.UTF-8
# echo 'export export LC_ALL=C' >> /home/vagrant/.profile
sudo dpkg --add-architecture i386

# enable multiverse and backports
#  echo 'deb http://archive.ubuntu.com/ubuntu trusty multiverse' >> /etc/apt/sources.list
#  echo 'deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse' >> /etc/apt/sources.list

# install python versions
# sudo add-apt-repository --yes ppa:deadsnakes/ppa
sudo apt-get update
#sudo apt-get install -y python2.7-dev
#sudo apt-get install -y python3.6-dev
# sudo apt-get install -y python3.7-dev
# sudo apt-get install -y python3.8-dev
# sudo apt-get install -y python3-distutils
# sudo apt-get install -y python3.9-dev
# sudo apt-get install -y python3.9-distutils

# tools
sudo apt-get install -y mc python3-pip xvfb

# eagle
#sudo apt-get install -y eagle:i386
TEMP_DEB=$(mktemp --suffix .deb)
wget -O $TEMP_DEB 'http://archive.ubuntu.com/ubuntu/pool/multiverse/e/eagle/eagle_6.6.0-2_i386.deb'
sudo apt-get install -y $TEMP_DEB

# project dependencies
sudo apt-get install -y scrot povray python-pil xserver-xephyr

# test dependencies
sudo python3 -m pip install tox

# doc dependencies
sudo apt-get install -y npm xtightvncviewer
sudo npm install -g npx
