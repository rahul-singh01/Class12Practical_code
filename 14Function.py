# Uses of Function in Python.

import random

def picker():

    with open('test.txt','r') as f:

        c = f.read().split(' ')
    
    n = random.randint(0,len(c))

    l = []

    for i in c:
        l.append(i)

    print('Random name found is',l[n])


def string():
    # searching into a string.  

    with open('test.txt','r') as f:
        t = f.read().split(' ')
    

    def search(x): # parameter is in the brackets

        for i in t:
            if  i == x:

                print("word found named!! ", x)

    x  = input('Enter the word you want to find = ')
    search(x)


# Main Program

ch = 'y'

while ch[0]=='y' or ch[0]=='Y':

    x = int(input(' press 1 for random generation of names \n press 2 for searching name in file \n Enter your choice = '))

    if x == 1:
        picker()

    elif x == 2:
        string()

    else:
        print('Invalid Operation !!')
    
    ch = input('Do you want more calculations? y/n = ')

print('-------------------------------------------------- Program Exit -------------------------------------------------------')

  


