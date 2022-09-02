# write a program to display odd number of a list.
l=int(input("enter the lower limit:"))
u=int(input("enter the upper limit:"))
for i in range(l,u+1):
    if(i%2==0):
        print(i,"is even number")
    
    elif(i%2)!=0:
        print(i,"is odd number")
    print()         

