from .PrinterBase import PrinterBase


class BasicPrinter(PrinterBase):

    printer_name = 'basic'
    _print_width = 40

    def print(self, output: str) -> None:
        if self._closed:
            raise RuntimeError('Printer is Closed.')
        end = ''

        l = len(output)
        if len(output) > self._print_width:
            self._print_width = l

        output += (self._print_width - l) * " "
        print(f'\r{output}', end=end, flush=True)

    def close(self):
        print('\r')
        self._closed = True
