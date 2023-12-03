import pytest

from utils.dicts import get_val

d = {1: 'one', 2: 'two'}


@pytest.mark.parametrize('dictionary, key, res', [
    (d, 1, 'one'),
    (d, 2, 'two'),
    (d, 3, 'git'),
])
def test_get_val(dictionary, key, res):
    assert get_val(dictionary, key) == res

# def test_get_val():
#     assert get_val(d, 1) == 'one'
#     assert get_val(d, 3, 'dflt') == 'dflt'
