
# Raspberry Pi Network Discord Monitor 🚀

A lightweight **network monitoring and alert system** built for **Raspberry Pi 5** that detects devices connecting and disconnecting from your network and sends real-time notifications through Discord.

The system continuously monitors your local network, identifies devices using MAC addresses, detects manufacturers, attempts automatic device name discovery, tracks connection history, and runs automatically in the background using a Linux system service.

---

# ✨ Features

## 🔔 Real-Time Alerts

Receive Discord notifications when:

* 🟢 A device connects to your network
* 🔴 A device disconnects from your network

Example:

```
🟢 DEVICE ONLINE

📱 Name: iPhone.local
🏭 Manufacturer: Apple Inc.
🌐 IP Address: 192.168.1.25
🔑 MAC Address: AA:BB:CC:DD:EE:FF
```

---

# 🔍 Device Discovery

The monitor automatically detects:

* Device IP address
* MAC address
* Manufacturer/vendor
* Hostname (when available)
* Connection status
* Last seen information

Supported discovery methods:

* ARP network scanning
* MAC vendor lookup
* mDNS discovery
* NetBIOS hostname detection

---

# 🏠 Use Cases

Perfect for:

* Home network monitoring
* IoT device tracking
* Raspberry Pi security projects
* Unknown device detection
* Learning Python networking
* Small network visibility

---

# 🧰 Hardware Requirements

## Recommended

* Raspberry Pi 5
* Raspberry Pi OS
* Network connection (Ethernet or Wi-Fi)

## Software

* Python 3
* Scapy
* Discord Webhook
* Linux systemd

---

# 📁 Project Structure

```
network-monitor/

├── network_alert.py          # Main monitoring script
├── requirements.txt          # Python dependencies
├── config.example.py         # Example configuration
│
├── install/
│   ├── install.sh            # Installation script
│   └── uninstall.sh          # Removal script
│
├── service/
│   └── network-alert.service # Auto-start service
│
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/network-monitor.git

cd network-monitor
```

Run the installer:

```bash
chmod +x install/install.sh

./install/install.sh
```

---

# 🔧 Configuration

Open the main configuration:

```bash
nano network_alert.py
```

Change:

```python
NETWORK = "192.168.1.0/24"

DISCORD_WEBHOOK = "YOUR_DISCORD_WEBHOOK_URL"
```

Example:

```python
NETWORK = "192.168.0.0/24"

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/..."
```

---

# ▶️ Running the Monitor

Start:

```bash
sudo systemctl start network-alert
```

Enable automatic startup:

```bash
sudo systemctl enable network-alert
```

Check status:

```bash
sudo systemctl status network-alert
```

View live logs:

```bash
sudo journalctl -u network-alert -f
```

---

# 🔄 How It Works

```
        Device Connects
              |
              |
              v
      Raspberry Pi Scanner
              |
              |
              v
   MAC + IP + Hostname Lookup
              |
              |
              v
       Discord Notification
```

---

# 🔐 Security Notes

* Only monitor networks you own or have permission to manage.
* Keep your Discord webhook private.
* Do not upload your personal configuration files.
* Use `.gitignore` to protect sensitive data.

---

# 🚀 Future Improvements

Planned features:

* Web dashboard
* SQLite database
* Device history graphs
* Mobile notifications
* Router API integration
* Unknown device blocking
* Email alerts
* Docker support

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

# 📜 License

MIT License

Free to use, modify, and share.

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
