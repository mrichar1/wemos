from machine import Pin
import time

button_a = Pin(0, Pin.IN)
button_b = Pin(2, Pin.IN)

print("Push button A or B...")
while True:
  if not button_a():
    print("A")
    time.sleep_ms(400)

  if not button_b():
    print("B")
    time.sleep_ms(400)


