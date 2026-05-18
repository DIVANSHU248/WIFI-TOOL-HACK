import time
import sys
import random
import json

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except:
        return {"animation_speed": 0.08, "max_wordlist_attempts": 20}

def show_banner():
    try:
        with open("banner.txt", "r") as f:
            print(f.read())
    except:
        print("======= WIFI-CRACKER =======")

def loading_bar(speed):
    for i in range(101):
        time.sleep(speed / 2)
        sys.stdout.write(f"\r[+] Cracking Packets... [{i}%] " + "#" * (i // 5))
        sys.stdout.flush()
    print("\n")

# Settings Load Karo
config = load_config()
speed = config.get("animation_speed", 0.08)

# 1. Display Banner
show_banner()
time.sleep(1)

print("[*] Initializing Wi-Fi card adapter...")
time.sleep(1)
print(f"[*] Switching interface to {config.get('default_interface', 'wlan0mon')}...")
time.sleep(1.5)

print("\n[*] Scanning for nearby networks...")
time.sleep(2)

# Scanned List
networks = ["JioFiber_5G_Secure", "Airtel_Xstream_2.4G", "Free_Public_WiFi"]
print("[+] Available Networks Found:")
for idx, net in enumerate(networks, 1):
    print(f"  {idx}. {net}")
    time.sleep(0.4)

print("")
target = input("[?] Enter Target Wi-Fi Name (SSID): ")
if not target.strip(): target = networks[0]

print(f"\n[*] Target Locked On: {target}")
print("[*] Capturing WPA2/WPA3 Handshake... Please wait.")
time.sleep(2)

print("\n[*] Launching Wordlist Attack using 'passwords.txt'...")
time.sleep(1)

# 2. Passwords Database se Fake Brute Force
try:
    with open("passwords.txt", "r") as f:
        passwords = [line.strip() for line in f.readlines()]
except:
    passwords = ["12345678", "password", "admin123"]

attempts = min(len(passwords), config.get("max_wordlist_attempts", 25))
for idx in range(attempts):
    sys.stdout.write(f"\r[-] Trying password [{idx+1}/{attempts}]: {passwords[idx]}")
    sys.stdout.flush()
    time.sleep(speed * 2)

print("\n\n[+] Handshake Match Found Successfully!")
loading_bar(speed)

# Final Display
print("=" * 55)
print("🎉 STATUS: NETWORK CRACKED SUCCESSFULLY! 🎉")
print("=" * 55)
print(f"Target Network : {target}")
print(f"Password Key   : {random.choice(passwords)}")
print(f"Encryption     : WPA2-PSK [AES]")
print("=" * 55)

