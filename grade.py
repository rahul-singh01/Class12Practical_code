# grade selection.
ch='y'
while ch=='y' or ch=='Y':
    a=int(input("Enter marks of English="))
    b=int(input("Enter marks of computer science="))
    c=int(input("Enter marks of physics="))
    d=int(input("Enter marks of chemistry="))
    e=int(input("Enter marks of maths="))
    p=(a+b+c+d+e)/5
    
    if(p>=75):
        print("first division")
    elif(p>=50):
        print("second division")
    elif(P>=33):
        print("thiird division")
    elif(p<=33):
        print("fail")
    else:
        print("invalid operation!")
   
    ch=input("do you want more claculatiions y/n")
print("thanks for using")
