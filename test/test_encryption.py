import pytest
import random
import string


from itertools import cycle
from io import BytesIO


@pytest.fixture
def read_file():
    return open('cipher.txt', 'rb').read()

def xore(data, key):
    return bytes(a^b for a, b in zip(data, cycle(key)))

def xor_decrypt(encrypted_text,key):
    with BytesIO(encrypted_text) as f:
        return xore(f.read(), key)


def guess_key(encrypted_text, key_size):
    guessAttempts = 0
    myPassword = input("Enter a password for the computer to try and guess: ")
    while True:
        guessAttempts = guessAttempts + 1
        key = ''.join([random.choice(string.ascii_letters + string.digits)for n in range(key_size)])
        print(key)
        decrypted = xor_decrypt(encrypted_text, key)
        if isEnglish(decrypted):
            print(decrypted)
            print("Password guessed successfully!")
            print("It took the computer %s guesses to guess your password." % (guessAttempts))
            break
        
    return {key: decrypted}


def test_cypher(read_file):
    raw = read_file
    decrypted = (xor_decrypt(raw,b'123'))
    print(decrypted)

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True