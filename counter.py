import argparse
import os
import subprocess
import sys
import time
import re


# Regular Expressions

DAYS_REGEX = re.compile(r'(\d+)(\s)*(d|days|dys|Days|Dys)')
HOURS_REGEX = re.compile(r'(\d+)(\s)*(h|hours|hrs|Hours|Hrs)')
MINUTES_REGEX = re.compile(r'(\d+)(\s)*(m|minutes|mins|Minutes|Mins)')
SECONDS_REGEX = re.compile(r'(\d+)(\s)*(s|secs|Seconds|Secs)')


# Decompose input str into days minutes and seconds

class Counter:

    def __init__(self, INPUT_STR, increment=1):
        daysMatch = DAYS_REGEX.search(INPUT_STR)
        hoursMatch = HOURS_REGEX.search(INPUT_STR)
        minutesMatch = MINUTES_REGEX.search(INPUT_STR)
        secondsMatch = SECONDS_REGEX.search(INPUT_STR)

        self.increment = increment
        self.stopped = False
        self.MATCHES = (daysMatch, hoursMatch, minutesMatch, secondsMatch)

    def tick(self):
        time.sleep(self.increment)
        self.timeLeft -= self.increment

    def get_time_left_str(self):
        return f'{int(self.timeLeft/3600):02d}:{int(self.timeLeft/60)%60:02d}:{self.timeLeft%60:02d}'

    def run(self):
        if not(self.stopped):
            timeParts = [0, 0, 0, 0]
            self.running = True

            for i in range(0, 4):
                if self.MATCHES[i] != None:
                    timeParts[i] = int(self.MATCHES[i].group(1))

            days, hours, minutes, seconds = timeParts

            self.timeLeft = 86400*days + 3600*hours + 60*minutes + seconds

            if self.timeLeft == 0:
                raise TimeFormatException("Invalid time string entered.")
                exit(0)
        else:
            self.stopped = False

        print("\nTimer Started")
        while self.timeLeft > 0 and self.running:
            print(self.get_time_left_str(), end='\r', flush=True)
            self.tick()
            

    def pause(self):
        print("\nTimer Paused")
        self.stopped = True
    



class TimeFormatException(Exception):
    pass
