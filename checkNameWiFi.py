# Program pertama kali masuk ke laman WiFi

import subprocess

output = subprocess.check_output("netsh wlan show interfaces")
output = output.decode("utf-8")

start = output.find("SSID") + 6
end = output.find("\n", start)

wifi_name = output[start:end].strip()

print("Connected to WiFi network:", wifi_name)