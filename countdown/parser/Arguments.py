
from dataclasses import dataclass
from typing import TypedDict

from ..alarm import AlarmBase
from ..printer import PrinterBase


class CountdownArguments(TypedDict):
    duration: float
    printer: PrinterBase
    alarm: AlarmBase
