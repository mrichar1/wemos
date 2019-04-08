from machine import freq
from esp import deepsleep
from umqtt.robust import MQTTClient
import time
import network
from hx711 import HX711
from config import Config

conf = Config()[__name__]

# Enable the HX711 (64x amp, data=4, sck=5 (d2, d1)
freq(160000000)

scale = HX711(4,5,channel=HX711.CHANNEL_A_64)
scale.power_on()
weight = scale.read()
scale.power_off()

# Wait for network up before proceeding
wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    time.sleep_ms(10)

client = MQTTClient(**conf)
client.connect(clean_session=False)

client.publish("{}/{}/{}".format(conf["client_id"], "sensor", "hx711"), str(weight), qos=1)

# Uncomment this to enable deep sleeping
deepsleep(600 * 1000000)
