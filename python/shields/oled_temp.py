from time import sleep
from machine import I2C, Pin
import ssd1306
from sht30 import SHT30

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(64, 48, i2c)

sensor = SHT30()

while True:
    temp, humid = sensor.measure()
    # Clear the screen
    display.fill(0)
    display.text("T:{:.2f}C".format(temp), 0, 0)
    display.text("H:{:.2f}%".format(humid), 0, 20)
    display.show()
    sleep(3)

