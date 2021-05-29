
class PrinterError(Exception):
    @classmethod
    def NoMatchingPrinter(cls, name: str):
        return cls(f'Unable to find printer matching name: {name}.')
