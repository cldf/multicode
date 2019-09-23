import unicodedata

import pytest

from multicode import recode
from multicode.__main__ import _recode


@pytest.mark.parametrize(
    "input,expected",
    [
        ('ɂ', 'ʔ'),
        ('a\u200Ab', 'a b'),
        # whitespace is collapsed:
        ('a \u200A b', 'a b'),
        ('ɂ\u200Ab', 'ʔ b'),
        ('ab cd e\nf gh', None),
        ('ab cd\u200Ae\nf gh', 'ab cd e\nf gh'),
    ]
)
def test_recode(input, expected):
    assert recode(input) == (input if expected is None else expected)


def test_cli_recode(capsys, mocker):
    in_ = unicodedata.normalize('NFD', 'äöü')
    _recode(mocker.Mock(args=[in_]))
    out, err = capsys.readouterr()
    assert out.startswith(in_)
