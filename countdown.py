   #! usr/bin/python3
   # countdown.py - A simple countdown script.

import argparse
import os
import subprocess
import sys
import time
import re

if sys.version_info < (3,0):
    print('Python 3 required')
    exit(1)
else:

    from counter import Counter, TimeFormatException

    
    FILE_DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))
    SOUND_FILE_PATH = os.path.join(FILE_DIRECTORY_PATH,'alarm.wav')

    # Take arguments

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('time',help='The amount of time to countdown in seconds', type=str)
    ARGS = PARSER.parse_args()

    INPUT_STR = ARGS.time

    # Run timer for specified length of countdown
    counter = Counter(INPUT_STR)
    while True:
        try:
            counter.run()
            break
        except KeyboardInterrupt:
            counter.pause()
            try:
                user_input = input("Press any key to continue\n")
            except KeyboardInterrupt:
                print("\nTimer Terminated")
                exit(0)
        except TimeFormatException:
            print("Invalid time string entered.")
            exit(1)

    #  At the end of the countdown, play a sound file.


    os.system(f'play -V0 -q {SOUND_FILE_PATH}')
    print('Time has elapsed')


