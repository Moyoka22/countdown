from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Dict, Type

from ..errors import PrinterError

_printer_registry: Dict[str, Type[PrinterBase]] = {}


def register_printer(name: str, printer: Type[PrinterBase]):
    _printer_registry[name] = printer


def get_printer(name: str) -> Type[PrinterBase]:
    try:
        printer = _printer_registry[name]
    except KeyError:
        raise PrinterError.NoMatchingPrinter(name)
    return printer


class PrinterBaseMeta(ABCMeta):
    def __new__(cls, name, bases, dict):
        klass = super().__new__(cls, name, bases, dict)
        printer_name = klass.__name__
        try:
            printer_name = klass.printer_name  # type: ignore
        except:
            pass

        register_printer(printer_name, klass)  # type: ignore
        return klass


class PrinterBase(metaclass=PrinterBaseMeta):
    _closed = False

    @abstractmethod
    def print(self, output: str) -> None:
        pass

    @abstractmethod
    def close(self):
        pass

    def is_closed(self):
        return self._closed
