import numpy as np

from itertools import cycle
from validate_englist_text import englishFreqMatchScore, next


MAX_MARK_FOR_TEXT_MATCHING_ENGLISH = 12

def xor_decrypt(data, key):
    return ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(data, cycle(key))])

def guess_key(encrypted_text, key_size):
    res = {}
    key = []
    key_str = ''
    decrypted = ''
    guessAttempts = 0

    while len(key_str) <= key_size and englishFreqMatchScore(decrypted) < MAX_MARK_FOR_TEXT_MATCHING_ENGLISH:
        guessAttempts += 1
        key = next(key, key_size)
        key_str = ''.join(key)
        decrypted = xor_decrypt(encrypted_text, key)
        if englishFreqMatchScore(decrypted) > 10:
            print("Password guessed successfully!")
            print("It took the computer %s guesses to guess your password." % (guessAttempts))
            res = {key_str: decrypted}
    return res


if __name__ == '__main__':
    buf = [chr(x) for x in np.loadtxt('cipher.txt', delimiter=',', dtype=np.integer)]
    print(guess_key(buf, 3))
