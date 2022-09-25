import string


englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
                    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
                    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
                    'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
ALLOWED_CHARACTERS = string.ascii_lowercase
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def next(key, key_size):
    if len(key) <= 0:
        for _ in range(key_size):
            key.append(indexToCharacter(0))
    else:
        key[0] = indexToCharacter((characterToIndex(key[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(key[0]) == 0:
            return list(key[0]) + next(key[1:], key_size)
    return key

def count_letters(text):
      result = {}
      for letter in text.lower():
        if letter not in result:
          result[letter] = 1
        else:
          result[letter] += 1
      return result

def getLetterCount(message):
    letterCount = {x:0 for x in string.ascii_uppercase}

    for letter in message.upper():  
        if letter in string.ascii_uppercase:   
            letterCount[letter] += 1    

    return letterCount

def getItemAtIndexZero(x):
    return x[0]

def getFrequencyOrder(message): 
    letterToFreq = getLetterCount(message)  
    freqToLetter = {}   
    for letter in string.ascii_uppercase:  
        if letterToFreq[letter] not in freqToLetter:    
            freqToLetter[letterToFreq[letter]] = [letter]   
        else:   
            freqToLetter[letterToFreq[letter]].append(letter)   

    for freq in freqToLetter:   
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)  
        freqToLetter[freq] = ''.join(freqToLetter[freq])    

    freqPairs = list(freqToLetter.items())  
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)    

    freqOrder = []  
    for freqPair in freqPairs:  
        freqOrder.append(freqPair[1])   

    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)  
    matchScore = 0  
    for commonLetter in ETAOIN[:6]: 
        if commonLetter in freqOrder[:6]:   
            matchScore += 1 
    for uncommonLetter in ETAOIN[-6:]:  
        if uncommonLetter in freqOrder[-6:]:    
            matchScore += 1 
    
    score = 6
    if matchScore > score:
        score = matchScore
    return matchScore
