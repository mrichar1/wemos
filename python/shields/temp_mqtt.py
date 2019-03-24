from machine import deepsleep, ADC
from umqtt.robust import MQTTClient
import time
import network
from sht30 import SHT30

client_id = "wemos"
server = "pi.lan"
port = 1883
user = "mqtt"
password = "password"
topic = "{}/{}".format(client_id, "sensor")
sensor = SHT30()
# Connect to ADC pin (A0)
adc = ADC(0)

# Wait for network up before proceeding
wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    time.sleep_ms(10)

client = MQTTClient(client_id, server, port=port, user=user, password=password)
client.connect(clean_session=False)

temp, humidity = sensor.measure()
client.publish("{}/{}".format(topic, "temperature"), str(temp), qos=1)
client.publish("{}/{}".format(topic, "humidity"), str(humidity), qos=1)
client.publish("{}/{}".format(topic, "moisture"), str(adc.read()), qos=0)

# Uncomment this if wrapped by timeout.py
#deepsleep()
