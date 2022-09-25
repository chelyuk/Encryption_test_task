import pytest

from validator.validate_englist_text import characterToIndex, indexToCharacter, next, count_letters, englishFreqMatchScore


@pytest.mark.parametrize('int, char',
                        [(0, 'a'),
                        (25, 'z'),
                        (10, 'k')])
def test_characterToIndex(int, char):
    assert int == characterToIndex(char)

@pytest.mark.parametrize('int, char',
                        [(0, 'a'),
                        (25, 'z'),
                        (10, 'k')])
def test_indexToCharacter(int, char):
    assert char == indexToCharacter(int)

@pytest.mark.parametrize('key, next_key, key_size',
                        [(['a'], ['b'], 1),
                        (['z'],['a','a'], 1),
                        (['z','z'], ['a','a','a'], 1),
                        (['y','k','l','b'],['z','k','l','b'], 4),
                        (['a','a','a'], ['b','a','a'], 3)])
def test_next(key, next_key, key_size):
    assert next(key,key_size) == next_key

@pytest.mark.parametrize('text, letters',
                        [('Hello, world!', {' ': 1, '!': 1, ',': 1, 'd': 1,
                                            'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1})])
def test_count_letters(text, letters):
    assert count_letters(text) == letters

@pytest.mark.parametrize('message, mark',
                        [('Some text', 3),
                        ('hope this text will be enough for my test', 6)])
def test_englishFreqMatchScore(message, mark):
    assert englishFreqMatchScore(message) == mark
