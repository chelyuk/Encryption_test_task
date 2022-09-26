from asyncore import read
import imp
import re
import pytest
import numpy as np

from decryptor.decrypt import guess_key
from validator.validate_english_text import englishFreqMatchScore


@pytest.fixture
def read_file():
    return guess_key([chr(x) for x in np.loadtxt('cipher.txt', delimiter=',', dtype=np.integer)], 3)

def test_decryption(read_file):
    assert  list(read_file.keys())[0] == 'mob'

def test_text(read_file):
    res = list(read_file.values()).pop()
    assert res.isascii()
    assert englishFreqMatchScore(res) >= 10
