#!/bin/bash

echo "Installing Raspberry Pi Network Monitor"


sudo apt update


sudo apt install -y \
python3-pip \
avahi-utils \
samba-common-bin


echo "Installing Python packages"

pip3 install -r requirements.txt


echo "Installing system service"


sudo cp service/network-alert.service /etc/systemd/system/


sudo systemctl daemon-reload


sudo systemctl enable network-alert.service


echo ""
echo "Installation complete"
echo ""
echo "Start service:"
echo "sudo systemctl start network-alert"
