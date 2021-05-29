import time
import threading
from typing import Type

from .alarm import AlarmBase
from .printer import FormatTime, PrinterBase


class Countdown(threading.Thread):
    TICK_INCREMENT = 0.01
    PRINT_INCREMENT = 1

    def __init__(self, duration: float,
                 Printer: Type[PrinterBase],
                 Alarm: Type[AlarmBase]):
        super().__init__(target=self.mainloop, args=(), name='countdown')
        self._duration = duration
        self._remaining = duration
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()
        self._unpause_event = threading.Event()
        self._printer = Printer()
        self._alarm = Alarm()
        self._formatter = FormatTime()
        self._last_print = time.perf_counter()

    def mainloop(self):
        while not self._stop_event.is_set():
            if self._pause_event.is_set():
                self._unpause_event.wait()
            self._tick()
            self._output()
        if self.has_remaining():
            self._printer.print('Stopped.')
            self._printer.close()
        else:
            self._printer.close()
            self._alarm.sound()

    def is_paused(self):
        return self._pause_event.is_set()

    def pause(self):
        self._output(message=' Paused.')
        self._pause_event.set()
        self._unpause_event.clear()

    def unpause(self):
        self._unpause_event.set()
        self._pause_event.clear()

    def reset(self, unpause=False):
        self._remaining = self._duration
        self._stop_event.clear()
        if unpause:
            self.unpause()

    def end(self):
        self.unpause()
        if self.has_remaining():
            self._printer.print('Stopped.')
        self._stop_event.set()

    def has_remaining(self) -> bool:
        return not self._remaining <= 0

    def _tick(self):
        self._wait()
        if not self._pause_event.is_set():
            self._remaining -= self.TICK_INCREMENT
        if not self.has_remaining():
            self.end()

    def _output(self, message=None):
        if (time.perf_counter() - self._last_print) < self.PRINT_INCREMENT:
            return
        self._last_print = time.perf_counter()

        if not self._pause_event.is_set():
            output = self._formatter.format(str(self._remaining))
            if message:
                output += f' {message}'
            self._printer.print(output)

    def _wait(self):
        time.sleep(self.TICK_INCREMENT)
