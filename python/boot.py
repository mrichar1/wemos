# This file is executed on every boot (including wake-boot from deepsleep)

from sleep_check import sleep_check
from timeout import Timeout

# Don't sleep if D5 is grounded
sleep_check()

# Start global timeout (deepsleep if main code blocks)
# Sleep after 10s, wake again after 5 min
Timeout(action="deepsleep", delay=10, wake_after=600)

### Start main code here...
import temp_mqtt
