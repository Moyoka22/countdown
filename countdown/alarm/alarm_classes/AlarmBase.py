from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Dict, Type

from ..errors import AlarmError

_alarm_registry: Dict[str, Type[AlarmBase]] = {}


def register_alarm(name: str, printer: Type[AlarmBase]):
    _alarm_registry[name] = printer


def get_alarm(name: str) -> Type[AlarmBase]:
    try:
        alarm = _alarm_registry[name]
    except KeyError:
        raise AlarmError.NoMatchingAlarm(name)
    return alarm


class AlarmBaseMeta(ABCMeta):
    def __init__(self, name, bases, dict):
        alarm_name = self.__name__
        try:
            alarm_name = self.alarm_name  # type: ignore
        except:
            pass
        register_alarm(alarm_name, self)


class AlarmBase(metaclass=AlarmBaseMeta):

    @abstractmethod
    def sound(self) -> None:
        pass
