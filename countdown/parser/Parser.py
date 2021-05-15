from argparse import Namespace

from .Arguments import Arguments
from .errors import ParseError


class Parser:
    def __init__(self, script_args: Namespace):
        try:
            self.printer_choice = script_args.printer
            self.alarm_choice = script_args.alarm_choice
            self.duration = script_args.duration

    def get_arguments(self) -> Arguments:
        pass
