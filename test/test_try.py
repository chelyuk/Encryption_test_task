import string
import numpy as np

from itertools import cycle


englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
                    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
                    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
                    'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALLOWED_CHARACTERS = string.ascii_lowercase
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)


def xor_decrypt(data, key) -> str:
    return ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(data, cycle(key))])

def guess_key(encrypted_text, key_size) -> dict:
    res = {}
    key = []
    key_str = ''
    decrypted = ''
    guessAttempts = 0

    while len(key_str) <= key_size and englishFreqMatchScore(decrypted) < 12:
        guessAttempts = guessAttempts + 1
        key = next(key)
        key_str = ''.join(key)
        decrypted = xor_decrypt(encrypted_text, key)
        if englishFreqMatchScore(decrypted) > 10:
            print("Password guessed successfully!")
            print("It took the computer %s guesses to guess your password." % (guessAttempts))
            res = {key_str: decrypted}
    return res

def characterToIndex(char) -> int:
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index) -> list:
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def next(key) -> list:
    """ Get next sequence of characters.
    Treats characters as numbers (0-255). Function tries to increment
    character at the first position. If it fails, new character is
    added to the back of the list.
    It's basically a number with base = 256.
    :param string: A list of characters (can be empty).
    :type string: list
    :return: Next list of characters in the sequence
    :rettype: list
    """
    if len(key) <= 0:
        for i in range(3):
            key.append(indexToCharacter(0))
    else:
        key[0] = indexToCharacter((characterToIndex(key[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(key[0]) is 0:
            return list(key[0]) + next(key[1:])
    return key

def count_letters(text) -> int:
      result = {}
      # Go through each letter in the text
      for letter in text:
        # Check if the letter needs to be counted or not
        if letter not in result:
          result[letter.lower()] = 1
        # Add or increment the value in the dictionary
        else:
          result[letter.lower()] += 1
      return result

def getLetterCount(message) -> int:

    # Returns a dictionary with keys of single letters and values of the    
    # count of how many times they appear in the message parameter. 
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
                'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0,
                'X': 0, 'Y': 0, 'Z': 0}  

    for letter in message.upper():  
        if letter in LETTERS:   
            letterCount[letter] += 1    

    return letterCount

def getItemAtIndexZero(x):
    return x[0]

def getFrequencyOrder(message) -> str: 
    # Returns a string of the alphabet letters arranged in order of most    
    # frequently occurring in the message parameter.    

    # first, get a dictionary of each letter and its frequency count    
    letterToFreq = getLetterCount(message)  

    # second, make a dictionary of each frequency count to each letter(s)   
    # with that frequency   
    freqToLetter = {}   
    for letter in LETTERS:  
        if letterToFreq[letter] not in freqToLetter:    
            freqToLetter[letterToFreq[letter]] = [letter]   
        else:   
            freqToLetter[letterToFreq[letter]].append(letter)   

    # third, put each list of letters in reverse "ETAOIN" order, and then   
    # convert it to a string    
    for freq in freqToLetter:   
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)  
        freqToLetter[freq] = ''.join(freqToLetter[freq])    

    # fourth, convert the freqToLetter dictionary to a list of tuple    
    # pairs (key, value), then sort them    
    freqPairs = list(freqToLetter.items())  
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)    

    # fifth, now that the letters are ordered by frequency, extract all 
    # the letters for the final string  
    freqOrder = []  
    for freqPair in freqPairs:  
        freqOrder.append(freqPair[1])   

    return ''.join(freqOrder)

def englishFreqMatchScore(message) -> int:

    # Return the number of matches that the string in the message   
    # parameter has when its letter frequency is compared to English    
    # letter frequency. A "match" is how many of its six most frequent  
    # and six least frequent letters is among the six most frequent and 
    # six least frequent letters for English.   
    freqOrder = getFrequencyOrder(message)  

    matchScore = 0  
    # Find how many matches for the six most common letters there are.  
    for commonLetter in ETAOIN[:6]: 
        if commonLetter in freqOrder[:6]:   
            matchScore += 1 
    # Find how many matches for the six least common letters there are. 
    for uncommonLetter in ETAOIN[-6:]:  
        if uncommonLetter in freqOrder[-6:]:    
            matchScore += 1 
    
    score = 6
    if matchScore > score:
        score = matchScore
    return matchScore

if __name__ == '__main__':
    raw = np.loadtxt('cipher.txt', delimiter=',', dtype=np.integer)
    buf = [chr(x) for x in raw ]
    print(guess_key(buf, 3))
