"""Set a timer that will reset/sleep after a timeout.

This is designed to prevent 'stuck' code from running forever.

delay = time before action
action = "exit" or "deepsleep"
wake_after = if sleeping, time before waking
"""

import machine
from esp import deepsleep

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
        self.timer.init(mode=machine.Timer.ONE_SHOT,
                   period=1000 * self.delay,
                   callback=lambda cb: deepsleep(1000000 * (self.wake_after + self.delay)))

    def deinit(self):
        self.timer.deinit()
