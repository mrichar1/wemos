from time import sleep
from machine import I2C, Pin
import ssd1306

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(64, 48, i2c)

while True:
    # Clear the screen
    display.fill(0)
    display.text("Top", 0, 0)
    display.show()
    sleep(2)
    display.text("Middle", 0, 20)
    display.show()
    sleep(2)
    display.text("Bottom", 0, 40)
    display.show()
    sleep(2)

