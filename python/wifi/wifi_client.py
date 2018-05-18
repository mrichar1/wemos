import network

sta_if = network.WLAN(network.STA_IF)

# Enable wifi client
if not sta_if.isconnected():
    print('connecting to wifi network...')
    sta_if.active(True)
    sta_if.connect('ssid', 'password', timeout=5000)
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())
