
import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
from typing import *

from pydub import AudioSegment
from pydub.playback import play

ROOT_DIR = Path(__file__).parents[1].absolute()
SOUNDS_DIR = ROOT_DIR / 'assets' / 'sounds'


@dataclass
class CountdownDuration:
    days: int
    hours: int
    minutes: int
    seconds: int


class StoreCountdownDurationAction(argparse.Action):
    """Resolves a duration tuple from the input string if a valid string is passed to the script"""
    DAYS_REGEX = re.compile(r'(\d+)(\s)*(d|days|dys|Days|Dys)')
    HOURS_REGEX = re.compile(r'(\d+)(\s)*(h|hours|hrs|Hours|Hrs)')
    MINUTES_REGEX = re.compile(r'(\d+)(\s)*(m|minutes|mins|Minutes|Mins)')
    SECONDS_REGEX = re.compile(r'(\d+)(\s)*(s|secs|Seconds|Secs)')

    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: Any, option_string: Optional[str] = None) -> CountdownDuration:
        values_str = " ".join(values)
        daysMatch = int(mo.group(1)) if (
            mo := self.DAYS_REGEX.search(values_str)) else 0
        hoursMatch = int(mo.group(1)) if (
            mo := self.HOURS_REGEX.search(values_str)) else 0
        minutesMatch = int(mo.group(1)) if (
            mo := self.MINUTES_REGEX.search(values_str)) else 0
        secondsMatch = int(mo.group(1)) if (
            mo := self.SECONDS_REGEX.search(values_str)) else 0
        setattr(namespace, self.dest, CountdownDuration(
            daysMatch, hoursMatch, minutesMatch, secondsMatch))


def play_sound():
    subprocess.run(
        ['ffplay', str(SOUNDS_DIR / 'alarm.wav'), '-nodisp', '-autoexit', '-loglevel', 'quiet'], shell=False)
