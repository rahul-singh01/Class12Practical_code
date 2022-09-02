# stack, loads the data from the end point and read it from the end only.


def push_stack():

    r = int(input("Enter yur roll no.=  "))

    name=input("Enter your name = ")

    a=(r,name)

    s.append(a)

def pop_stack():

    if (s==[]):

        print("stack empty")

    else:
        r,name=s.pop(0)

        print("Deleted Roll Number and Name is :",r,name)

def display_stack():

    if (s==[]):

        print("stack empty")

    else:

        for i in range(len(s)-1,-1,-1):

            print(s[i])       

#main program

s = []

ch  = 'y'

while ch[0]=='y' or ch[0]=='Y':

    print("1. Push")

    print("2. Pop")

    print("3. Display")

    ch=int(input("Enter your choice"))

    if ch== 1 :

        push_stack()

    elif(ch==2):
        pop_stack()

    elif(ch==3) :

        display_stack()

    else:

        print("!!!!Wrong Input!!!!")

    ch = input("Do you want to proceed 'y or 'n ")
    
print('Program Exit')
    













    
