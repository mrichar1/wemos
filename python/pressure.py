from bmp180 import BMP180
from machine import I2C, Pin
bus =  I2C(scl=Pin(5), sda=Pin(4), freq=100000)   # on esp8266
bmp180 = BMP180(bus)
