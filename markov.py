
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


#            listvalue = [dictionary.get(word)]
#            print(listvalue)
#            value = []
#            for x in range(len(listvalue)):
#                value.append(listvalue[x][0])
#            value = listvalue[0]
#            print(value)
#            value.append(words[words.index(word)+1])
#            dictionary.update({word:value})
#            values.append(words[words.index(word)+1])
#            dictionary.update({word:values})
    print (dictionary)

train("My milkshake brings all the boys to the yard and they're like, it's better than yours damn right it's better than yours")
