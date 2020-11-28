#! /usr/bin/python3
# countdown.py - A simple countdown script.

import argparse
from time import sleep
from typing import *

from countdown.printers import Printer, CursesPrinter
from countdown.utils import CountdownDuration, StoreCountdownDurationAction, play_sound


class CountdownTimer:
    def __init__(self, duration: CountdownDuration, PrinterClass: Printer, REFRESH_RATE=1):
        self._seconds_remaining = duration.days * 86400 + duration.hours * \
            3600 + duration.minutes * 60 + duration.seconds
        self.duration = duration
        self.printer_factory = PrinterClass
        self.printer = PrinterClass()
        self.REFRESH_RATE = REFRESH_RATE
        self.tick = 1 / REFRESH_RATE

    @staticmethod
    def format_time(time):
        return f'{time // 3600:02.0f}:{time % 3600 // 60:02.0f}:{time % 60:02.0f}'

    def get_time_remaining(self, formatted=True):
        if formatted:
            return CountdownTimer.format_time(self._seconds_remaining)
        return self._seconds_remaining

    def start(self):
        if self.printer.closed:
            del self.printer
            self.printer = self.printer_factory()

        try:
            while self._seconds_remaining > 0:
                self._seconds_remaining -= self.tick
                formatted_string = f'{self._seconds_remaining // 3600:02.0f}:{self._seconds_remaining % 3600 // 60:02.0f}:{self._seconds_remaining % 60:02.0f}'
                self.printer.print(formatted_string)
                sleep(self.tick)
        except:
            raise
        finally:
            self.printer.close()


def main(args: Dict[str, Any] = None, PrinterClass: Printer = CursesPrinter) -> None:
    if not args:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            'time', action=StoreCountdownDurationAction, type=str, nargs="+")
        args = vars(parser.parse_args())
    duration = args.get('time')
    timer = CountdownTimer(duration, PrinterClass)

    while 1:
        try:
            timer.start()
            play_sound()
            exit(0)
        except KeyboardInterrupt:
            stop = input(
                f'\rStopped at {timer.get_time_remaining()} remaining. Exit? [y/N]: ')
            if stop.upper() == 'Y':
                exit(1)


if __name__ == "__main__":
    main()
