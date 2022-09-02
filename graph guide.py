# Graph Representation.
import matplotlib.pyplot as plt
print("this will only work on linear graphs")
c=int(input("enter the value of the constant="))
a=input("enter the given first variable of equation such as{a,x,y}=")
b=input("enter the given second variable of equation such as{a,x,y}=")
d=int(input("enter the coefficient of first variable if there is no coefficient simply input 1="))
e=int(input("enter the coefficient of second variable if there is no coefficient simply input 1="))
f= str(d)+a
g= str(e)+b
h=input("the operator between the equation such as sum, substract=")
if h=='sum' or h=='+':
    print("your equation is",f,'+',g,"=",c)
    print("equating points of the line......")
    print("at x=1")
    i=-c/(e*1)
    print("y co-ordinates",i)
    print("at x=2")
    i1=-c/(e*2)
    print("y co-ordinates",i1)
    print("at x=3")
    i2=-c/(e*3)
    print("y co-ordinates", i2)
    print("at x=4")
    i3=-c/(e*4)
    print("y co-ordinates", i3)
    plt.plot(1, 2, 3, 4, label="x co-ordinates")
    plt.plot(i, i1, i2,i3, label="y co-ordinates")
    plt.legend()
    plt.show()

elif h=='substract' or h=='-':
    print("your equation is", f, '-', g, "=", c)
    print("equating points of the line......")
    # let x=0
    i=-1*(c/e)
    print("y co-ordinates",'-',i)
    # let y=0
    j=-1*(c/d)
    print("x co-ordinates",'-',j)
    k = 0
    plt.plot(k, i, label="x co-ordinates")
    p = 0
    plt.plot(j, p, label="y co-ordinates")
    plt.legend()
    plt.show()

else:
    print("invalid input!!!!! check the above statements")
