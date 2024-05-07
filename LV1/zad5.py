file = open('SMSSpamCollection.txt')
ham = []
spam = []
hamcounter = 0
spamcounter = 0
hamwords = 0
spamwords = 0
countendswith = 0
for line in file:
    if line.startswith('spam'):
        spamcounter += 1
        spamwords += len(line.split()[1:])
        if(line.strip().endswith('!')):
            countendswith +=1
    if line.startswith('ham'):
        hamcounter += 1
        hamwords += len(line.split()[1:])


print(spamwords/spamcounter)
print(hamwords/hamcounter)



print('Broj poruka u tipu spam koje završavaju sa "!": ', countendswith)