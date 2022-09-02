# count the number of words in tut.txt, tut1.txt, tut2.txt, 

ch='y'
while ch[0]=='y' or ch[0]=='Y':

    print("\n To count the number of words \n")
    x = input("Choose 1 for tut.txt \n choose 2 for tut1.txt \n choose 3 for tut3.txt \n choose = ")

    if x == '1':
        file = open('tut.txt', 'r')
        for i  in file:
            count = i.split(' ')
        print('Number of words in file are ',len(count))

    elif x == '2':
        file = open('tut1.txt', 'r')
        for i in file:
            count = i.split(' ')
        print('Number of words in file are ',len(count))

    elif x == '3':
        file = open('tut2.txt', 'r')
        for i  in file:
            count = i.split(' ')
        print('Number of words in file are ',len(count))

    ch = input('Do you want to Calculate more y/n ')
print('Thanks For Using')