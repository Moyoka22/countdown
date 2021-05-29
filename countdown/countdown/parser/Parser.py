import re
from typing import Any, Dict, List, Tuple, Type, TypedDict, cast

from ..alarm import AlarmBase, get_alarm
from ..printer import PrinterBase, get_printer
from .errors import ParseError

valid_tokens = [r'\b\d+[hms]\b', r'\b\d+\s?(?:hour|minute|second)s?\b']


class CountdownArguments(TypedDict):
    duration: float
    Printer: Type[PrinterBase]
    Alarm: Type[AlarmBase]


class Parser:
    UNIT_MAP = {
        'second': 1,
        'seconds': 1,
        's': 1,
        'minute': 60,
        'm': 60,
        'minutes': 60,
        'hour': 3600,
        'hours': 3600,
        'h': 3600
    }

    def __init__(self, script_args: Dict[str, Any]):
        self.printer_choice = script_args.get('printer')
        if not self.printer_choice:
            raise ParseError.MissingArgument('printer')
        self.alarm_choice = script_args.get('alarm')
        if not self.alarm_choice:
            raise ParseError.MissingArgument('alarm')
        self.duration_str = script_args.get('duration')
        if not self.duration_str:
            raise ParseError.MissingArgument('duration')

    def get_arguments(self) -> CountdownArguments:
        self.duration_str = cast(str, self.duration_str)
        self.printer_choice = cast(str, self.printer_choice)
        self.alarm_choice = cast(str, self.alarm_choice)
        return {
            'duration': self.get_duration(self.duration_str),
            'Printer': self.get_printer(self.printer_choice),
            'Alarm': self.get_alarm(self.alarm_choice)
        }

    def get_duration(self, duration_str: str) -> float:
        return self._parse_duration_string(duration_str)

    def get_printer(self, printer_choice: str) -> Type[PrinterBase]:
        return get_printer(printer_choice)

    def get_alarm(self, alarm_choice: str) -> Type[AlarmBase]:
        return get_alarm(alarm_choice)

    def _parse_duration_string(self, duration_str: str) -> float:
        tokens = self._lex_duration_string(duration_str)
        quanta = self._make_quanta(tokens)

        duration = 0
        for quantum in quanta:
            duration += quantum[0] * Parser.UNIT_MAP[quantum[1]]
        return duration

    @staticmethod
    def _lex_duration_string(duration_str: str) -> List[str]:
        tokens = []
        for valid_token in valid_tokens:
            tokens += re.findall(valid_token, duration_str, re.IGNORECASE)
        return tokens

    @staticmethod
    def _make_quanta(tokens: List[str]) -> List[Tuple[float, str]]:
        quanta: List[Tuple[float, str]] = []
        for token in tokens:
            amount = float(re.findall(re.compile('\d+'), token)[0])
            time_unit = re.findall(re.compile('[^0-9]'), token)[0].strip()
            quanta.append((amount, time_unit))
        return quanta
