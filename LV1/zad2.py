try:
    grade = float(input('Unesite ocjenu:  '))
    if(grade < 0.6 and grade >= 0):
        print('F')
    elif(grade >= 0.6 and grade < 0.7):
        print('D')
    elif(grade >= 0.7 and grade < 0.8):
        print('C')
    elif(grade >= 0.8 and grade < 0.9):
        print('B')
    elif(grade >= 0.9 and grade <= 1):
        print('A')
    else:
        print('Unešeni broj nije između 0.0 i 1.0')
except:
    print('Unešeni broj nije između 0.0 i 1.0')