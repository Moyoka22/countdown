
from countdown.parser.Parser import Parser


def test_lex_duration_string():
    test_input = 'ashdf 40m  afsda 60hours asdf 5 second 20 hour 5day 2minute'

    test_parser = Parser({
        'duration': object(),
        'printer': object(),
        'alarm': object()
    })
    expected_output = ['40m', '60hours', '5 second', '20 hour', '2minute']

    assert test_parser._lex_duration_string(test_input) == expected_output
