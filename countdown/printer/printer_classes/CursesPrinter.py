import curses

from art import text2art

from .PrinterBase import PrinterBase


class CursesPrinter(PrinterBase):
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.win = curses.newwin(200, 200, 0, 0)

    def print(self, output: str) -> None:
        if self.closed:
            raise RuntimeError('Printer is Closed.')
        self.win.clear()
        art = text2art(output).split("\n")
        for i in range(len(art)):
            self.win.addstr(i, 0, art[i], curses.COLOR_BLUE)
        self.win.refresh()

    def close(self):
        del self.win
        curses.endwin()
        self.closed = True
