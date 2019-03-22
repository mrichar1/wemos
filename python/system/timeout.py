"""Set a timer that will reset/sleep after a timeout.

This is designed to prevent 'stuck' code from running forever.

delay = time before action
action = "exit" or "deepsleep"
wake_after = if sleeping, time before waking
"""

import machine

class Timeout():

    def __init__(self, delay=60, action="reset", wake_after=600):
        self.delay = delay
        self.wake_after = wake_after
        self.timer = machine.Timer(-1)
        getattr(self, action)()

    def reset(self):
        self.timer.init(mode=machine.Timer.ONE_SHOT,
                   period=1000 * self.delay,
                   callback=lambda cb: machine.reset())

    def deepsleep(self):
        rtc = machine.RTC()
        rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
        rtc.alarm(rtc.ALARM0, 1000 * (self.wake_after + self.delay))
        self.timer.init(mode=machine.Timer.ONE_SHOT,
                   period=1000 * self.delay,
                   callback=lambda cb: machine.deepsleep())

