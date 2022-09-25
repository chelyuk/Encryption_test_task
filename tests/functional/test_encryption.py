import pytest


@pytest.fixture
def read_file():
    return open('cipher.txt', 'rb').read()
