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
v
Discord Alert





