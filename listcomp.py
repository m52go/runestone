# playing with list comprehensions

wordlist = ['cat','dog','rabbit']

# i'd never write this long of a list comprehension in real life, but i wanted
# to see if it was possible to do everything in one shot
letterlist = [letter for word in wordlist for letter in word if (''.join([word for word in wordlist]).count(letter) < 2)]

print(letterlist)
