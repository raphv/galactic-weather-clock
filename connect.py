import network
import time
import gc
import WIFI_CONFIG

def isconnected():
    return network.WLAN(network.STA_IF).isconnected()

def connect():
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(WIFI_CONFIG.SSID,WIFI_CONFIG.PSK)
    for seconds in range(12):
        isconnected = sta.isconnected()
        print('Connected' if isconnected else 'Waiting for connection')
        if isconnected:
            ip = sta.ifconfig()[0]
            print(ip)
            return
        time.sleep(1)