from abc import ABCMeta, abstractmethod
import curses
from typing import *

from art import text2art


class Printer(metaclass=ABCMeta):
    closed = False

    @abstractmethod
    def print(self, output: str) -> None:
        ...

    def close(self):
        self.closed = True


class ConsolePrinter(Printer):
    def print(self, output: str) -> None:
        print('\r' + output, end='', flush=True)


class CursesPrinter(Printer):
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
