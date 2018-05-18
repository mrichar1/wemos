from machine import Pin
import time

button_a = Pin(0, Pin.IN, Pin.PULL_UP)
button_b = Pin(2, Pin.IN, Pin.PULL_UP)

def debounce(pin):
    # Do something
    print("PUSH:", pin)
    time.sleep_ms(400)

button_a.irq(trigger=Pin.IRQ_FALLING, handler=debounce)
button_b.irq(trigger=Pin.IRQ_FALLING, handler=debounce)

print("Push button A (pin0) or B (pin2)...")


