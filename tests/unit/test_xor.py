import pytest

from decryptor.decrypt import xor_decrypt


@pytest.mark.parametrize('data, key',
                        [('My best string', 'key'),
                        ('Very very long test string', 'small key')] )
def test_xor(data, key):
    assert data == xor_decrypt(xor_decrypt(data, key), key)
