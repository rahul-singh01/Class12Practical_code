
# queue is a linear data structure,
#stores items in First In First Out (FIFO) manner

# QUEUE

def queue_enqueue():

    r=int(input("ENTER YOUR ROLL NUMBER = "))

    name=input(" ENTER YOUR NAME = ")

    c= (r, name)

    a.append(c)

def queue_dequeue():

    if(a==[]):

        print("QUEUE IS EMPTY")

    else:
        print("DELETED DATA IS: ",a.pop(0))


def queue_display():

    if (a==[]):

        print("QUEUE IS EMPTY")

    for i in range(0, len(a)):

        print(a[i])

        

#main program

a=[]

c = 'y'

while(c == 'y' or c == 'Y'):

    print("1. ENQUEUE ")

    print("2. DEQUEUE")

    print("3. DISPLAY")

    ch=int(input("ENTER YOUR CHOICE = "))

    if(ch==1):

        queue_enqueue()

    elif(ch==2):

        queue_dequeue()

    elif(ch==3):

        queue_display()

    else:
        print(" WRONG CHOICE!!!!1")

    c=input("DO YOU WANT TO PROCEED 'Y' OR 'N = ")

print('Program Exit')
