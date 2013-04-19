# infinite monkey theorem using a hill-climb algorithm

import string
import random

def genstring():
    letterstring = string.letters[:26] + ' '
    randstring = ''
    for i in range(28):
        randstring += random.choice(letterstring)
    return randstring

def genchar():
    letterstring = string.letters[:26] + ' '
    return random.choice(letterstring)

def accuracy(sample):
    correct = 'methinks it is like a weasel'
    good = 0
    correctarr = []
    for i in range(len(correct)):
        if correct[i] == sample[i]:
            correctarr.append(True)
        else:
            correctarr.append(False)
    return correctarr

def executer():
    currstring = beststring = genstring()
    curracc = accuracy(currstring)
    bestacc = curraccint = sum(curracc)
    for i in range(1000):
        print(beststring)
        for j in range(len(curracc)):
            if curracc[j]:
                pass
            else:
                currstring = currstring[:j] + genchar() + currstring[(j+1):]
                curraccint = sum(accuracy(currstring))
                if curraccint > bestacc:
                    bestacc = curraccint
                    beststring = currstring
                    if curraccint == 28:
                        return("DONE! " + str(i) + ": " + currstring)
        curracc = accuracy(currstring)
    return("Not quite: " + str(bestacc) + ": " + str(beststring))

print(executer())
