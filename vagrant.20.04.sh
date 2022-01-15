#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
sudo update-locale LANG=en_US.UTF-8 LANGUAGE=en.UTF-8
# echo 'export export LC_ALL=C' >> /home/vagrant/.profile
sudo dpkg --add-architecture i386

# enable multiverse and backports
#  echo 'deb http://archive.ubuntu.com/ubuntu trusty multiverse' >> /etc/apt/sources.list
#  echo 'deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse' >> /etc/apt/sources.list

# install python versions
sudo add-apt-repository --yes ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.8-dev
sudo apt-get install -y python3-distutils
sudo apt-get install -y python3.9-dev
sudo apt-get install -y python3.9-distutils
sudo apt-get install -y python3.10-dev
sudo apt-get install -y python3.10-distutils

# tools
sudo apt-get install -y mc python3-pip xvfb

# eagle
#sudo apt-get install -y eagle:i386
TEMP_DEB=$(mktemp --suffix .deb)
wget -O $TEMP_DEB 'http://archive.ubuntu.com/ubuntu/pool/multiverse/e/eagle/eagle_6.6.0-2_i386.deb'
dpkg-deb -x $TEMP_DEB /tmp/PackageFolder
dpkg-deb --control $TEMP_DEB /tmp/PackageFolder/DEBIAN
sed -i -e 's/libssl1.0.0/libssl1.1/g' /tmp/PackageFolder/DEBIAN/control
dpkg -b /tmp/PackageFolder /tmp/eagle.deb
sudo apt-get install -y /tmp/eagle.deb
sudo ln -s /usr/lib/i386-linux-gnu/libssl.so.1.1 /usr/lib/i386-linux-gnu/libssl.so.1.0.0
sudo ln -s /usr/lib/i386-linux-gnu/libcrypto.so.1.1 /usr/lib/i386-linux-gnu/libcrypto.so.1.0.0

# project dependencies
sudo apt-get install -y scrot povray python-pil xserver-xephyr

# test dependencies
sudo python3 -m pip install tox

# doc dependencies
sudo apt-get install -y npm xtightvncviewer
sudo npm install -g npx
