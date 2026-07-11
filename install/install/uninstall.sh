#!/bin/bash

echo "Removing Network Monitor"


sudo systemctl stop network-alert.service

sudo systemctl disable network-alert.service


sudo rm /etc/systemd/system/network-alert.service


sudo systemctl daemon-reload


echo "Network Monitor removed"
