file = open('SMSSpamCollection.txt')
ham = []
spam = []
for line in file:
    line = line.rstrip()
    words = line.split()
    if(line.startswith('ham')):
        for word in words:
            if(word != 'ham'):
                ham.append(word)
    if(line.startswith('spam')):
        for word in words:
            if(word != 'spam'):
                spam.append(word)
countham = 0
for word in ham:
    countham= countham + len(word)
print('Prosječan broj riječi u tipu ham: ', countham/len(ham))
countspam = 0
for word in spam:
    countspam = countspam + len(word)
print('Prosječan broj riječi u tipu spam: ', countspam/len(spam))

countendswith = 0
for line in file:
    line = line.rstrip()
    if(line.endswith('!')):
        countendswith = countendswith + 1

print('Broj poruka u tipu spam koje završavaju sa "!": ', countendswith)
print(ham)