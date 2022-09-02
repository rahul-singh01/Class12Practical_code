
# Adding or Dispalying from file
# patient.txt is the text file 

import time

localtime=time.asctime(time.localtime(time.time()))


def adding():
    file = open('patient.txt','a')
    a  = input('Enter the name of the patient = ')
    b =  input('Enter the bed no. = ')
    c = input('Enter the room no. = ')
    d = input('Enter disease name = ')
    file.write(f'Pateint Name = {a} || Bed no. = {b} || Room no. = {c} || disease name = {d} || Admitted on {localtime} \n\n')
    file.close()
    
def display():
    file  =  open('patient.txt','r')
    print(file.read())
    file.close()

#main
    
ch = 'y'
while ch[0]=='y' or ch[0]=='Y':

    x = int(input(' TO ADD A PATIENT PRESS 1 \n TO DISPLAY PATIENT INFO PRESS 2 \n CHOOSE = '))

    if x == 1:
        adding()
        
    elif x == 2:
        display()
        
    else:
        print('Invalid operations! ')  
    
    ch = input('Want to proceed y/n = ')  

print("Thanks for using! ")
     
     
