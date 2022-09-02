main_number=18
number_of_guess=9
r=0
ch='y'
while ch=='y' or ch=='Y':
    while(number_of_guess):
        r=r+1
        n=int(input("enter the number="))
        if n > 18:
            print("you are far away from ur ans")
        elif n < 18:
            print("you are too close t your answer")
        elif n == 18:
            print("you won")
            print("number of attempt=",str(r))
            break
        else:
            print("enter the valid inputs")
        number_of_guess=number_of_guess-1
        print("remaining number of guesses", str(number_of_guess))
    ch=input("do you want to play more y/n=")
print("thanks for playing")



