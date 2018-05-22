# Be sure to connect GPIO16 (D0) to RST or this won't work!
import machine

# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
seconds = 10
rtc.alarm(rtc.ALARM0, 1000 * seconds)

# put the device to sleep
machine.deepsleep()

# Optionally add the following to boot.py for sleep detection
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('power on or hard reset')
