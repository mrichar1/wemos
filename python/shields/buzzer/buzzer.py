from machine import Pin, PWM
from time import sleep

beep_pin = Pin(14)

while True:
    beeper = PWM(beep_pin, freq=600, duty=868)
    sleep(1)
    beeper.deinit()
  

