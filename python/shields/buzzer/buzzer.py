from machine import Pin, PWM
import time

beep_pin = Pin(14)

beeper = PWM(beep_pin)
beeper.duty(868)

def beeps(i):
    beeper.freq(i)
    time.sleep_ms(5)


for i in range(100,1000):
    beeps(i)
for i in range(1000,100,-1):
    beeps(i)

beeper.deinit()
