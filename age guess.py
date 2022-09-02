ch='y'
while ch=='y' or ch=='Y':
    n=int(input("Enter your age="))
    if(n<18):
        print("you are not allowed to drive!!!!!!!!!!")
    elif(n>18):
        print("you are allowed to drive")
    elif(n==18):
        print("attempt some test to qualify")
    else:
        print("invalid information!!!!")
    ch=input("do you want more calculations y/n=")
print("thanks for using")
