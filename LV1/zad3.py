list = []
while(True):
    number = input('Unesi broj ili "Done": ')
    if number == 'Done':
        break
    elif number.isalpha():
        print('Morate unjeti broj!')
    else:
        list.append(float(number))
print(len(list))
print(sum(list)/len(list))
print(max(list))
print(min(list))