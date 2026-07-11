# network-monitor
# Raspberry Pi Network Discord Monitor

A lightweight network monitoring system built for Raspberry Pi 5 that detects devices connecting and disconnecting from your local network and sends real-time alerts through Discord.

The tool continuously scans your network, identifies connected devices, detects manufacturers from MAC addresses, attempts automatic device name discovery, and stores device history for tracking.

## Features

- 🟢 Real-time device online alerts
- 🔴 Device offline alerts
- 💬 Discord webhook notifications
- 🔍 Automatic network device discovery
- 🏭 MAC address manufacturer detection
- 📱 Automatic hostname/device name detection
- 🌐 IP address tracking
- 🔑 MAC address tracking
- 💾 Device history storage
- 🔄 Runs automatically after Raspberry Pi reboot using systemd
- ⚡ Designed for Raspberry Pi 5 and Raspberry Pi OS

## How It Works

Network Device Connects
|
v
Raspberry Pi Scanner
|
v
Device Information Detection## Example Alert


🟢 DEVICE ONLINE

📱 Name: iPhone.local
🏭 Manufacturer: Apple Inc.
🌐 IP: 192.168.1.150
🔑 MAC: AA:BB:CC:DD:EF:FE
|
## Requirements

- Raspberry Pi 5
- Raspberry Pi OS
- Python 3
- Discord account with webhook access

## Use Cases

- Home network monitoring
- IoT device tracking
- Unauthorized device detection
- Small network security monitoring
- Learning network programming with Python

## Disclaimer

This tool is intended for monitoring networks you own or have permission to manage. Always respect privacy and local laws when monitoring network activity.


Discord Alert
raspberry-pi
python
network-monitoring
discord-bot
cybersecurity
iot
home-network
scapy
linux## Installation

Clone the repository:

```bash
git clone https://github.com/YOURNAME/network-monitor.git

cd network-monitor
automation













