from typing import Callable, List, Tuple

Test = str
ParsingFunction = Callable[[str], float]

duration_parsers: List[Tuple[Test, ParsingFunction]] = []
