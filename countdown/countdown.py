import time

from .printer import PrinterBase
from .alarm import AlarmBase


class Countdown:
    TICK_INCREMENT = 0.01

    def __init__(self, duration: float,
                 printer: PrinterBase,
                 alarm: AlarmBase):
        self._duration = duration
        self._remaining = duration
        self._finished = False
        self._printer = printer
        self._alarm = alarm

    def start(self):
        while not self._finished:
            self._tick()
            self._wait()
        self._alarm.sound()

    def _tick(self):
        self._remaining -= self.TICK_INCREMENT
        self._finished = (self._remaining == 0)

    def _wait(self):
        time.sleep(self.TICK_INCREMENT)
