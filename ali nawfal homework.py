import socket
import uuid
import subprocess
import re
import requests

class SystemInfo:
    def get_local_ip(self):
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip
        except Exception as e:
            return f"Error getting local IP: {e}"

    def get_public_ip(self):
        try:
            public_ip = requests.get("https://api.ipify.org").text
            return public_ip
        except Exception as e:
            return f"Error getting public IP: {e}"

    def get_mac_address(self):
        try:
            mac_num = hex(uuid.getnode()).replace('0x', '').upper()
            mac_address = ':'.join(mac_num[i:i+2] for i in range(0, 12, 2))
            return mac_address
        except Exception as e:
            return f"Error getting MAC address: {e}"

    def get_wifi_password(self):
        try:
            profiles_data = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
            profiles = re.findall("All User Profile     : (.*)", profiles_data)
            wifi_passwords = {}
            for profile in profiles:
                try:
                    results = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True, text=True)
                    password = re.search("Key Content            : (.*)", results)
                    wifi_passwords[profile] = password.group(1) if password else "No password found"
                except subprocess.CalledProcessError:
                    wifi_passwords[profile] = "Error retrieving password"
            return wifi_passwords
        except Exception as e:
            return f"Error getting Wi-Fi passwords: {e}"

if __name__ == "__main__":
    sys_info = SystemInfo()
    print("=== System Information Collector ===")
    print(f"Local IP Address  : {sys_info.get_local_ip()}")
    print(f"Public IP Address : {sys_info.get_public_ip()}")
    print(f"MAC Address       : {sys_info.get_mac_address()}")
    print("\nSaved Wi-Fi Passwords:")
    wifi_data = sys_info.get_wifi_password()
    if isinstance(wifi_data, dict):
        for network, password in wifi_data.items():
            print(f"  {network}: {password}")
    else:
        print(wifi_data)