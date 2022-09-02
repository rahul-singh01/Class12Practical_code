#USER DEFINED TABLE.
ch='y'
while ch=='y' or ch=='Y':
    n=int(input("Enter the value of required table="))
    for i in range(1,11):
        y=i*n
        print(n,"X",i,"=",y)
        
    ch=input("do you want more calculations y/n=")
print("thanks for using")
