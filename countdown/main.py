import argparse

from .Countdown import Countdown
from .parser import Arguments, Parser


def main(args: argparse.Namespace):

    countdown_args = Parser(args).get_arguments()

    countdown = Countdown(**countdown_args)


def parse_script_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_script_arguments()
    main(args)
