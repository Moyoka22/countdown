
from dataclasses import dataclass
from typing import TypedDict

from ..alarm import AlarmBase
from ..printer import PrinterBase


class CountdownArguments(TypedDict):
    duration: float
    printer: PrinterBase
    alarm: AlarmBase


@dataclass
class Arguments:
    def __init__(self, countdown: str,
                 printer_choice: str = 'basic',
                 alarm_choice: str = 'beep'):
        pass

    def as_dict(self) -> CountdownArguments:
        return {}
