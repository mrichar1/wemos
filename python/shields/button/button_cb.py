import time
from machine import Pin

def debounce(pin):
    # Do something
    print("PUSH")
    time.sleep_ms(300)

p = Pin(0, Pin.IN, Pin.PULL_UP)
p.irq(trigger=Pin.IRQ_FALLING, handler=debounce)
