   #! usr/bin/python3
   # countdown.py - A simple countdown script.

import argparse
import os
import subprocess
import time
import re

# Regular Expressions 

daysRegex = re.compile(r'(\d+)(\s)*(d|days|dys|Days|Dys)')
hoursRegex = re.compile(r'(\d+)(\s)*(h|hours|hrs|Hours|Hrs)')
minutesRegex = re.compile(r'(\d+)(\s)*(m|minutes|mins|Minutes|Mins)')
secondsRegex = re.compile(r'(\d+)(\s)*(s|secs|Seconds|Secs)')

# Take arguments

parser = argparse.ArgumentParser()
parser.add_argument('time',help='The amount of time to countdown in seconds', type=str)
args = parser.parse_args()

# Decompose input str into days minutes and seconds

inputStr = args.time

daysMatch = daysRegex.search(inputStr)
hoursMatch = hoursRegex.search(inputStr)
minutesMatch = minutesRegex.search(inputStr)
secondsMatch = secondsRegex.search(inputStr)

matches = [daysMatch,hoursMatch,minutesMatch,secondsMatch]

timeParts = [0,0,0,0]

for i in range(0,4):
    if matches[i] != None:
        timeParts[i] = int(matches[i].group(1))



days, hours, minutes, seconds = timeParts


timeLeft = 86400*days + 3600*hours + 60*minutes + seconds

if timeLeft==0:
    print("Invalid time string entered.")
    exit(0)

print("Timer Started")


while timeLeft > 0:

    timeLeftStr = "%02d:%02d:%02d" %(int(timeLeft/3600),int(timeLeft/60)%60,timeLeft%60)
    print(timeLeftStr, end='\r',flush=True)
    time.sleep(1)
    timeLeft = timeLeft - 1

#  At the end of the countdown, play a sound file.

os.system('play -V0 -q alarm.wav')
print("Time has elapsed")
exit(0)