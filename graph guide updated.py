import matplotlib.pyplot as plt
ch='y'
while(ch=='y' or ch=='Y'):
    try:
        print("this will only work on linear graphs")
        c = int(input("enter the value of the constant="))
        a = input("enter the given first variable of equation such as{a,x,y}=")
        b = input("enter the given second variable of equation such as{a,x,y}=")
        d = int(input("enter the coefficient of first variable if there is no coefficient simply input 1="))
        e = int(input("enter the coefficient of second variable if there is no coefficient simply input 1="))
        f = str(d) + a
        g = str(e) + b
        h = input("the operator between the equation such as sum, substract=")

        if h == 'sum' or h == '+':
            print("your equation is", f, '+', g, "=", c)
            print("equating points of the line......")
            print("at x=1")
            i = ((c - (d * 1)) / e)
            print("y co-ordinates", i)
            print("at x=2")
            i1 = ((c - (d * 2)) / e)
            print("y co-ordinates", i1)
            print("at x=3")
            i2 = ((c - (d * 3)) / e)
            print("y co-ordinates", i2)
            print("at x=4")
            i3 = ((c - (d * 4)) / e)
            print("y co-ordinates", i3)
            plt.bar([1, 2, 3, 4, ], [i, i1, i2, i3])
            plt.plot([1, 2, 3, 4, ], [i, i1, i2, i3])
            plt.xlabel('X Co-ordinates')
            plt.ylabel('Y Co-ordinates')
            plt.legend()
            plt.show()

        elif h == 'substract' or h == '-':
            print("your equation is", f, '-', g, "=", c)
            print("equating points of the line......")
            print("at x=1")
            i = -((c - (d * 1)) / e)
            print("y co-ordinates", i)
            print("at x=2")
            i1 = -((c - (d * 2)) / e)
            print("y co-ordinates", i1)
            print("at x=3")
            i2 = -((c - (d * 3)) / e)
            print("y co-ordinates", i2)
            print("at x=4")
            i3 = -((c - (d * 4)) / e)
            print("y co-ordinates", i3)
            plt.bar([1, 2, 3, 4, ], [i, i1, i2, i3])
            plt.plot([1, 2, 3, 4, ], [i, i1, i2, i3])
            plt.show()
            plt.legend()
        else:
            print("invalid input!!!!! check the above statements")
    except:
        print("you entered the wrong input")
    ch=input("do you want to try again y/n=")
print("thanks for using")
