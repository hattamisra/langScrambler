# Language scrambler
# This script makes up a fake language by scrambling up Indonesian sentences
# Good for making up fictional languages in RPG campaigns

import sys

# finds if the first letter of a word were capitalized
# so that the modified word will have the same capitalization
def firstLetterCapitalized(word):
    if word[0].isupper() == True and word.isupper() == False:
        return True
    else:
        return False 

# finds phomemes in a word (single letter or digraph) and converts it to another letter or digraph
def phomemeConverter(word):

    word = str.lower(word)

    digraphs = ["ng", "ny", "sy", "ts"]

    soundSwitch = {
            "sy": "c",
            "ts": "s",
            "ny": "ng",
            "ng": "g",
            "b": "d",
            "d": "b",
            "r": "l",
            "l": "r",
            "j": "y",
            "y": "j",
            "a": "o",
            "e": "a",
            "i": "u",
            "o": "e",
            "u": "i"
            }

    # create list to store input phomemes
    phomemes = list(word)

    # go through word to separate word into component phomemes
    i = 0

    while i < len(phomemes)-1 :

        possibleDigraph = phomemes[i] + phomemes[i+1]

        # if it is a digraph, combine the two phomemes
        if possibleDigraph in digraphs:
            phomemes[i:i+1] = "".join(phomemes[i:i+1])
            i = i+1
        else:
            i = i+1

    # now we have all the phomemes separated
    # time to convert the phomemes
    for m, n in enumerate(phomemes):
        if n in soundSwitch:
            phomemes[m] = soundSwitch[n]

    newWord = "".join(phomemes)

    return newWord

while True:

    sentence = input("Enter a sentence in Bahasa Indonesia. Press Enter to quit: ")

    # quits if the user only presses Enter
    if sentence == (""):
        sys.exit()
        break

    else:
        words = sentence.split()

        sentenceCaseWords = []
        upperCaseWords = []
        newWords = []

        # checks capitalization and phomemes of each word
        for word in words:
            
            sentenceCaseWords.append(firstLetterCapitalized(word))
            newWords.append(phomemeConverter(word))

            if word.isupper() == True:
                upperCaseWords.append(True)
            else:
                upperCaseWords.append(False) 
        
        for i, word in enumerate(newWords):

            # if the original word was in sentence case, turn new word into sentence case too
            if sentenceCaseWords[i] == True:
                newWords[i] = word.capitalize()

            # if the original word was in upper case, turn new word into upper case
            elif upperCaseWords[i] == True:
                newWords[i] = word.upper()
        
        # print a joined version of newWords
        print(" ".join(newWords))