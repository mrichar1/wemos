# Only runs code if pin 14 (D5) is high (i.e, not grounded)
# Ground this pin to abort code tht will deepsleep
from machine import Pin
from sys import exit

def sleep_check():
    allow_sleep = Pin(14, Pin.IN, Pin.PULL_UP)
    if not allow_sleep.value():
      exit()

