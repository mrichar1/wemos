# Be sure to connect GPIO16 (D0) to RST or this won't work!
import esp

seconds = 10
# Put machine to sleep - wake = usecs
esp.deepsleep(seconds * 1000000)

# Optionally add the following to boot.py for sleep detection
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('power on or hard reset')
