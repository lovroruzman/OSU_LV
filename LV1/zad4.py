file = open ('song.txt')
dictionary = {}
for line in file:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

count = 0
for word in dictionary:
    if dictionary[word] == 1:
        print(word)   
        count+=1

print(count) 


