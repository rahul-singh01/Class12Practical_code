ch='y'
while ch=='y' or ch=='Y':
    x=input("1.area of rectangle\n 2.area of circle\n 3.area of square\n")
    if(x=='1'):
        l=int(input("Enter the lenght of rectangle="))
        b=int(input("Enter the breadth of rectangle="))
        print("AREA OF RECTANGLE=",l*b)
    elif(x=='2'):
        r=int(input("Enter radius of the circle="))
        print("AREA OF CIRCLE=",3.14 * r**2)
    elif(x=='3'):
        s=int(input("Enter side of the square="))
        print("AREA OF SQUARE=",s**2)
    ch=input("do you want more calculations y\n")
print("Thanks for using!!")
             
         
    

