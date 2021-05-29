
class AlarmError(Exception):
    @classmethod
    def NoMatchingAlarm(cls, name: str):
        return cls(f'Unable to find alarm matching name: {name}.')
