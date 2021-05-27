from __future__ import annotations


class ParseError(Exception):

    @classmethod
    def MissingArgument(cls, arg: str) -> ParseError:
        return cls(f"Missing argument '{arg}'.")
