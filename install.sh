#!/bin/sh
echo "\033[32m--Updating ...\033[0m";
sudo apt-get -y update;

#sudo apt-get install -y python-tk;
#sudo apt-get install -y python-pip;
#sudo -H pip2 install --upgrade pip;
#sudo -H pip2 install networkx
#sudo -H pip2 install numpy;
#sudo -H pip2 install matplotlib;
#sudo -H pip2 install seaborn;

sudo apt-get install -y python3-tk;
echo "\033[32m--Updating ...\033[0m";
sudo apt-get install -y python3-pip;
echo "\033[32m--Upgrading ...\033[0m";
sudo -H pip3 install --upgrade pip;
echo "\033[32m--Installing pyrtlsdr ...\033[0m";
sudo -H pip3 install pyrtlsdr;
echo "\033[32m--Installing networkx ...\033[0m";
sudo -H pip3 install networkx
echo "\033[32m--Installing numpy ...\033[0m";
sudo -H pip3 install numpy;
echo "\033[32m--Installing matplotlib ...\033[0m";
sudo -H pip3 install matplotlib;
echo "\033[32m--Installing seaborn ...\033[0m";
sudo -H pip3 install seaborn;

#sudo apt-get install -y build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev libsqlite3-dev libpcre3-dev ethtool shtool rfkill zlib1g-dev libpcap-dev;
#sudo apt-get install -y aircrack-ng;
