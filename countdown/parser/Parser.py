from typing import Any, Dict, Type, TypedDict, cast

from ..alarm import AlarmBase
from ..printer import PrinterBase
from .errors import ParseError


class CountdownArguments(TypedDict):
    duration: float
    printer: Type[PrinterBase]
    alarm: Type[AlarmBase]


class Parser:
    def __init__(self, script_args: Dict[str, Any]):
        self.printer_choice = script_args.get('printer')
        if not self.printer_choice:
            raise ParseError.MissingArgument('printer')
        self.alarm_choice = script_args.get('alarm_choice')
        if not self.alarm_choice:
            raise ParseError.MissingArgument('printer')
        self.duration_str = script_args.get('duration')
        if not self.duration_str:
            raise ParseError.MissingArgument('duration')

    def get_arguments(self) -> CountdownArguments:
        self.duration_str = cast(str, self.duration_str)
        self.printer_choice = cast(str, self.printer_choice)
        self.alarm_choice = cast(str, self.alarm_choice)
        return {
            'duration': self.get_duration(self.duration_str),
            'printer': self.get_printer(self.printer_choice),
            'alarm': self.get_alarm(self.alarm_choice)
        }

    def get_duration(self, duration_str: str) -> float:
        pass

    def get_printer(self, printer_choice: str) -> Type[PrinterBase]:
        pass

    def get_alarm(self, alarm_choice: str) -> Type[AlarmBase]:
        pass
