from .PrinterBase import PrinterBase


class BasicPrinter(PrinterBase):

    printer_name = 'basic'

    def print(self, duration: float) -> None:
        end = ''
        if duration < 0:
            end = '\n'
            duration = 0
        duration_str = self._format_duration(duration)
        print(f'\r{duration_str}', end=end, flush=True)

    def _format_duration(self, duration: float) -> str:
        duration_seconds = int(duration % 60)
        duration_seconds_str = f'{duration_seconds:02d}'
        duration_minute = int(duration // 60) % 60
        duration_minute_str = f'{duration_minute:02d}:'
        duration_hour = int(duration // 3600)
        duration_hour_str = ''
        if duration_hour:
            duration_hour_str = f'{duration_hour}:'
        return f'{duration_hour_str}{duration_minute_str}{duration_seconds_str}'
