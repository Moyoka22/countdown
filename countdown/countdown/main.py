import argparse
from typing import Any, Dict

from .Countdown import Countdown
from .Listener import Listener
from .parser import Parser


def main(args: Dict[str, Any]):

    countdown_args = Parser(args).get_arguments()

    countdown = Countdown(**countdown_args)
    listener = Listener(countdown)

    countdown.start()
    listener.start()

    countdown.join()


def parse_script_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('duration', type=str,
                        help='A string specifying the duration for which the '
                        'timer should be run.')
    parser.add_argument('--printer', '-p', default='curses', type=str,
                        help='The printer to use for displaying the'
                        'remaining time.'
                        )
    parser.add_argument('--alarm', '-a', default='silent', type=str,
                        help='The alarm to ring when the timer is finished.')
    return parser.parse_args()


def entry():
    args = parse_script_arguments()
    main(vars(args))


if __name__ == '__main__':
    entry()
