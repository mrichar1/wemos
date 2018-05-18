from machine import Pin, PWM
from time import sleep

# https://github.com/rsc1975/micropython-sht30
from sht30 import SHT30

sensor = SHT30()

while True:
    temp, humidity = sensor.measure()
    print("TEMPERATURE: {} C".format(temp))
    print("HUMIDITY: {} %".format(humidity))
    sleep(2)
  

