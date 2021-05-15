import argparse
from typing import Any, Dict

from .Countdown import Countdown
from .parser import Parser


def main(args: Dict[str, Any]):

    countdown_args = Parser(args).get_arguments()

    countdown = Countdown(**countdown_args)


def parse_script_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_script_arguments()
    main(vars(args))
