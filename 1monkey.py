# infinite monkey theorem using brute force. #unpossible

import string
import random

def genstring():
    letterstring = string.letters[:26] + ' '
    randstring = ''
    for i in range(28):
        randstring += random.choice(letterstring)
    return randstring

def accuracy(sample):
    correct = 'methinks it is like a weasel'
    good = 0
    for i in range(len(correct)):
        if correct[i] == sample[i]:
            good += 1
    return good

def executer(tries):
    bestacc, curracc, beststring, currstring = 0, 0, '', ''
    for i in range(tries):
        currstring = genstring()
        curracc = accuracy(currstring)
        if curracc > bestacc:
            bestacc, beststring = curracc, currstring
            if bestacc == 28:
                print("finished!!")
                break;
    print("{} accuracy after {} tries. Best string: {}".format(bestacc, tries, beststring))

executer(100000)
