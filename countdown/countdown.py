import time
from typing import Type

from .printer import PrinterBase
from .printer.printer_classes import BasicPrinter
from .alarm import AlarmBase
from .alarm.alarm_classes import SilentAlarm


class Countdown:
    TICK_INCREMENT = 0.01

    def __init__(self, duration: float,
                 printer: Type[PrinterBase] = BasicPrinter,
                 alarm: Type[AlarmBase] = SilentAlarm):
        self._duration = duration
        self._remaining = duration
        self._finished = False
        self._printer = printer()
        self._alarm = alarm()

    def start(self):
        while not self._finished:
            self._tick()
            self._printer.print(self._remaining)
            self._wait()
        self._alarm.sound()

    def restart(self):
        self._remaining = self._duration
        self._finished = False

    def _tick(self):
        self._remaining -= self.TICK_INCREMENT
        self._finished = (self._remaining <= 0)

    def _wait(self):
        time.sleep(self.TICK_INCREMENT)
