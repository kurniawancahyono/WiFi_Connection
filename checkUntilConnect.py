import subprocess
import time

wifi = "Redmi"
connected = False
counter = 0

# Program konek ke WiFi & memilih network yang diinginkan

while not connected:
    global wifi_name
    output = subprocess.check_output("netsh wlan show interfaces")
    output = output.decode("utf-8")

    start = output.find("SSID") + 4
    end = output.find("\n", start)

    wifi_name = output[start:end].strip()
    wifi_name = wifi_name[2:]

    if wifi_name == "Redmi":
        connected = True
        print("Connected to WiFi network:", wifi_name)
        # return render template "Berhasil terhubung ke WiFi"
    else:
        print("Waiting Connection..")
        time.sleep(3)
        counter += 1
        if counter == 5:
            print("Times Up!")
            break
        # return render template "Tidak Berhasil Terhubung ke WiFi"