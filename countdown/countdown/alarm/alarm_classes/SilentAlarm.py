from .AlarmBase import AlarmBase


class SilentAlarm(AlarmBase):

    alarm_name = 'silent'

    def sound(self):
        print('Finished.')
