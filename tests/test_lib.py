import pytest

from ecarton_code_challenge.lib.convert import convert_chars

testdata = [
  [['a'], [970]],
  [['1'], [0]],
  [[None], [0]],
  [['z'], [0]],
]

@pytest.mark.parametrize('invalue,expected', testdata)
def test(invalue, expected):

    result = convert_chars(invalue)

    assert result == expected
