import machine
from umqtt.robust import MQTTClient
import time
import network
from sht30 import SHT30

client_id = "greenhouse"
server = "pi.lan"
port = 1883
user = "mqtt"
password = "fleurdelis"
topic = "{}/{}".format(client_id, "sensor")
sensor = SHT30()

# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# set RTC.ALARM0 to fire after X seconds (waking the device)
seconds = 600

# Wait for network up before proceeding
wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    time.sleep_ms(10)

client = MQTTClient(client_id, server, port=port, user=user, password=password)
client.connect(clean_session=False)

temp, humidity = sensor.measure()
client.publish("{}/{}".format(topic, "temperature"), str(temp), qos=1)
client.publish("{}/{}".format(topic, "humidity"), str(humidity), qos=1)
rtc.alarm(rtc.ALARM0, 1000 * seconds)
machine.deepsleep()
