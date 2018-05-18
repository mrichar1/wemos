import time
from machine import Pin

pin0 = Pin(0, Pin.IN, Pin.PULL_UP)


def callback(pin):
    # disable callback
    pin.irq(trigger=False)
    print("PUSH")
    time.sleep_ms(200)
    #re-enable callback
    irq(pin)

def irq(pin):
    pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

# Initial irq setup
irq(pin0)
print("Push the button!")
