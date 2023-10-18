import subprocess

wifi = "Redmi Note 10 Pro"
output = subprocess.check_output("netsh wlan show interfaces")

if wifi in output.decode("utf-8"):
    print("Connected to the correct WiFi network.")
else:
    print("Not connected to the correct WiFi network.")