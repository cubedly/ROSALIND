list_1 = 'We tried list and we tried dicts also we tried Zen'.split()

d = {}

for word in list_1:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1

for word, value in d.items():
    print (word + " " + str(value))
