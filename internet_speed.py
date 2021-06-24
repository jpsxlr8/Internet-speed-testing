import speedtest
wifi = speedtest.Speedtest()
print("Wifi upload speed is ",wifi.upload())
print("Wifi download speed is ",wifi.download())
