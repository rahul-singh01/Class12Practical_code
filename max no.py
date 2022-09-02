#Maximum number display program.
ch='y'
while ch=='y' or ch=='Y':
    a=int(input("Enter your first number="))
    b=int(input("Enter your second number="))
    c=int(input("Enter your third number="))
    if(a>b):
        print(a,"is the greater number")
    elif(c>b):
        print(c,"is the greatre number")
    elif(b>a):
        print(b,"is the greater number")
    elif(b>c):
        print(b,"is the greater number")
    else:
        print("INVALID OPERATION!!!")



        
    ch=input("do you want more calculations y/n=")
print("Thanks for using")
