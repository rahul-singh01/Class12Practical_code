#write a program to input name and marks of five subjects and display total marks and percentage marks.
ch='y'
while ch=='y' or ch=='Y':
    a=int(input("Enter marks of English="))
    b=int(input("Enter marks of computer science="))
    c=int(input("Enter marks of physics="))
    d=int(input("Enter marks of chemistry="))
    e=int(input("Enter marks of maths="))
    print("Total marks=",a+b+c+d+e)
    print("percentage marks=",((a+b+c+d+e)/5),"%")
    ch=input("do you want more claculatiions y/n")
print("thanks for using")
    
