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
    return dictionary
#    print (dictionary)

def generate(model, firstWord, numWords):
    sentence = ""
    word = firstWord
    for x in range(numWords):
        sentence += word + " "
#        print(model.get(word))
        word = random.choice(model[word])
    print(sentence)


sample = train("Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that")
generate(sample, "like", 10)

