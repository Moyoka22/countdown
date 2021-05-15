from abc import ABCMeta, abstractmethod

class PrinterBase(metaclass=ABCMeta):
    closed = False

    @abstractmethod
    def print(self, output: str) -> None:
        pass

    def close(self):
        self.closed = True