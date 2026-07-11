
#!/usr/bin/env python3

from scapy.all import ARP, Ether, srp
import requests
import time
import socket
import subprocess
import json
import os
from datetime import datetime
from mac_vendor_lookup import MacLookup


# ======================================
# CONFIGURATION
# ======================================

NETWORK = "192.168.1.0/24"

DISCORD_WEBHOOK = "YOUR_DISCORD_WEBHOOK_URL"

SCAN_INTERVAL = 60

DATABASE_FILE = "devices.json"



# ======================================
# DEVICE DATABASE
# ======================================

def load_database():

    if os.path.exists(DATABASE_FILE):

        with open(DATABASE_FILE, "r") as file:
            return json.load(file)

    return {}



def save_database():

    with open(DATABASE_FILE, "w") as file:

        json.dump(
            devices,
            file,
            indent=4
        )



devices = load_database()



# ======================================
# MANUFACTURER LOOKUP
# ======================================

mac_lookup = MacLookup()

try:
    mac_lookup.update_vendors()

except Exception:
    pass



def get_manufacturer(mac):

    try:
        return mac_lookup.lookup(mac)

    except:

        return "Unknown Manufacturer"



# ======================================
# DEVICE NAME DISCOVERY
# ======================================

def get_device_name(ip):


    # DNS hostname

    try:

        hostname = socket.gethostbyaddr(ip)[0]

        if hostname:
            return hostname

    except:

        pass



    # mDNS discovery

    try:

        result = subprocess.check_output(
            ["avahi-resolve", "-a", ip],
            timeout=3
        ).decode(errors="ignore")


        parts = result.split()

        if len(parts) > 1:
            return parts[1]


    except:

        pass



    # Windows NetBIOS

    try:

        result = subprocess.check_output(
            ["nmblookup", "-A", ip],
            timeout=3
        ).decode(errors="ignore")


        for line in result.splitlines():

            if "<00>" in line and "GROUP" not in line:

                return line.split()[0]


    except:

        pass



    return "Unknown Device"



# ======================================
# DISCORD ALERTS
# ======================================

def send_discord(message):

    try:

        requests.post(

            DISCORD_WEBHOOK,

            json={
                "content": message
            },

            timeout=5
        )

    except Exception as error:

        print(
            "Discord Error:",
            error
        )



# ======================================
# NETWORK SCAN
# ======================================

def scan_network():

    arp = ARP(
        pdst=NETWORK
    )


    ethernet = Ether(
        dst="ff:ff:ff:ff:ff:ff"
    )


    packet = ethernet / arp


    answered = srp(
        packet,
        timeout=3,
        verbose=False
    )[0]


    found_devices = {}


    for sent, received in answered:

        mac = received.hwsrc.upper()

        ip = received.psrc


        found_devices[mac] = ip


    return found_devices



# ======================================
# MONITOR LOOP
# ======================================

online_devices = {}


print(
    "🚀 Raspberry Pi Network Monitor Started"
)


send_discord(
    "✅ Raspberry Pi Network Monitor Started"
)



while True:


    current_devices = scan_network()



    # DEVICE ONLINE

    for mac, ip in current_devices.items():


        if mac not in online_devices:


            online_devices[mac] = ip


            name = get_device_name(ip)

            manufacturer = get_manufacturer(mac)


            now = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )


            devices[mac] = {

                "name": name,

                "manufacturer": manufacturer,

                "ip": ip,

                "first_seen": devices.get(mac, {}).get(
                    "first_seen",
                    now
                ),

                "last_seen": now

            }


            save_database()



            message = f"""
🟢 **DEVICE ONLINE**

📱 Name: **{name}**

🏭 Manufacturer: **{manufacturer}**

🌐 IP: `{ip}`

🔑 MAC: `{mac}`

⏰ Time: {now}
"""


            print(message)

            send_discord(message)




    # DEVICE OFFLINE

    for mac in list(online_devices.keys()):


        if mac not in current_devices:


            last_ip = online_devices[mac]


            info = devices.get(
                mac,
                {}
            )


            message = f"""
🔴 **DEVICE OFFLINE**

📱 Name: **{info.get('name','Unknown Device')}**

🏭 Manufacturer: **{info.get('manufacturer','Unknown')}**

🌐 Last IP: `{last_ip}`

🔑 MAC: `{mac}`

⏰ Time: {datetime.now()}
"""


            print(message)

            send_discord(message)


            del online_devices[mac]



    time.sleep(
        SCAN_INTERVAL
    )
