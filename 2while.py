
# Calculator using While loop

ch = 'y'

while ch[0]=='y' or ch[0]=='Y':

    a = int(input("Enter First Number= "))
    b = int(input("Enter Second Number= "))

    x = int(input('Choose 1 for Add \n Choose 2 for Substract \n Choose 3 for Divide \n Choose 4 for Multiply \n Choose = '))

    if x == 1:
        print('Add = ',a+b)

    elif x == 2:
        print('Substract = ',a-b)

    elif x == 3:
        print('Divide = ',a/b)
    
    elif x == 4:
        print('Multiply = ',a*b)
    
    else:
        print('Invalid Operations')
    
    ch = input('Do you want more calculations? y/n = ')
    
print("Thanks for Using!! ")

    