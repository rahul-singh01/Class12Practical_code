
# printing right triangle using for loop

h = int(input("Enter the height of triangle = "))

if h < 191:

    for  i in range(0,h):

        for j in range(0,i+1):

            print('*',end='')

        print('\r') 
else:
    print('Enter the limit lower than 191 to get best triangle')

