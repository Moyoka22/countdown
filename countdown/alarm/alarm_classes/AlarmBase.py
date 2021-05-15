from abc import ABCMeta, abstractmethod

class AlarmBase(metaclass=ABCMeta):

    @abstractmethod
    def sound(self) -> None:
        pass
