import curses

from art import text2art

from .PrinterBase import PrinterBase


class CursesPrinter(PrinterBase):
    printer_name = 'curses'

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self._win = curses.newwin(200, 200, 0, 0)

    def print(self, output: str) -> None:
        if self._closed:
            raise RuntimeError('Printer is Closed.')
        self._win.clear()
        art = text2art(output, font='lcd').split("\n")
        for index, a in enumerate(art, 0):
            self._win.addstr(index, 0, a, curses.COLOR_BLUE)
        self._win.refresh()

    def close(self):
        del self._win
        curses.endwin()
        self._closed = True
