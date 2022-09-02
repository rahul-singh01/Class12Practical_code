#faulty calculator.
repeat='y'
while repeat=='y'or repeat=='Y':
    print("welcome to faulty caculator some values in this calculator will shows wrong results")
    x = int(input("enter your first number="))
    y = int(input("enter your second number="))
    ch = input("what do you want to do sum(+), multiply(*), divide(/), substract(-)=")
    if ch == 'sum' or ch == "+":
        if x == 56 or y == 9:
            print("77")
        else:
            print("the sum is=", x + y)
    elif ch == 'multiply' or ch == '*':
        if x == 45 or y == 3:
            print("555")
        else:
            print("the product is", x * y)
    elif ch == 'divide' or ch == '/':
        if x == 56 or y == 6:
            print("4")
        else:
            print("the divide is", x / y)

    elif ch == 'substract' or ch == '-':
        if x == 40 or y == 6:
            print("78")
        else:
            print("the subtraction is", x - y)
    else:
        print("invalid information!!")
    repeat=input("do you want more calculations y/n=")
print("thanks for using")
