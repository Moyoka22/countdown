from .AlarmBase import AlarmBase


class SilentAlarm(AlarmBase):
    def sound(self):
        print('Finished.')
