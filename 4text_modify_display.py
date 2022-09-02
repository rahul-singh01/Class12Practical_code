
# modify and display text files
# tut1.txt is the file 

with open('tut1.txt','r') as f:
    t = f.read() 
ask = input('Do you want to see what is written in file y/n = ')
if ask[0]=='y' or ask[0]=='Y':
    print(t)

select = input('Enter the word from the text you want to replace or modify = ')

with open('tut1.txt','r') as f:
    t = f.read().split(' ')
for i in t:
    if select in i:
        pass
        
modify = input("Enter the word which you want to modify: ")

file = open("tut1.txt", "rt")
data = file.read()
data = data.replace(select, modify)
file.close()

fin = open("tut1.txt", "wt")
fin.write(data)
fin.close()

print('\n Modified Text \n ')
print(open('tut1.txt','r').read())

    


