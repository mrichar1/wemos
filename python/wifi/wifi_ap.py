import network

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
ap.config(essid='MYESSID', authmode=network.AUTH_WPA_WPA2_PSK, password="password")
print('network config:', ap_if.ifconfig())
