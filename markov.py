import random

def train(s):
    dictionary = dict()
    words = s.split(' ')
    for x in range(len(words)):
        word = words[x]
        if x == len(words)-1:
            if word not in dictionary:
                dictionary[word]=[words[0]]
            else:
                dictionary[word].append(words[0])
        elif word not in dictionary:
            dictionary[word]=[words[x+1]]
        else:
            dictionary[word].append(words[x+1])
    print (dictionary)

def generate(model, firstWord, numWords)
    sentence = firstWord
    for x in range(numWords):
        sentence += random.choice(dictionary.get() + " "
    print (sentence)


train("My milkshake brings all the boys to the yard and they're like, it's better than yours damn right it's better than yours")
