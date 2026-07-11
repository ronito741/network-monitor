#!/bin/bash

echo "Installing Raspberry Pi Network Monitor"


sudo apt update


echo "Installing required packages..."

sudo apt install -y \
python3-pip \
avahi-utils \
samba-common-bin


echo "Installing Python libraries..."

pip3 install -r requirements.txt


echo "Installing systemd service..."

sudo cp network-alert.service /etc/systemd/system/


sudo systemctl daemon-reload


sudo systemctl enable network-alert.service


echo "Installation complete!"

echo "Start the service with:"
echo "sudo systemctl start network-alert.service"
