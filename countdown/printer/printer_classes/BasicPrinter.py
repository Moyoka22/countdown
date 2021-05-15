from .PrinterBase import PrinterBase

class BasicPrinter(PrinterBase):
    def print(self, output: str) -> None:
        print('\r' + output, end='', flush=True)