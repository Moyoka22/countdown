import argparse
from typing import Any, Iterable, Optional


class JoinListAction(argparse.Action):
    """Returns the list of nargs as a single space separated string."""

    def __call__(self, parser: argparse.ArgumentParser,
                 namespace: argparse.Namespace, values: Any,
                 option_string: Optional[str] = None) -> None:
        if isinstance(values, Iterable):
            values = ' '.join(values)
        setattr(namespace, self.dest, values)
