
# Sorting by Insertion Method

ch = 'y'
l = []
while ch[0]=='y' or ch[0]=='Y':

    a = int(input("Enter the number = "))
    l.append(a)

    ch = input('Add more numbers y/n = ')
print()

if len(l)==1:
    print('please add atleast two numbers ')
else:
    for i in range(1,len(l)):
        k = l[i]
        j = i-1
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            j = j-1
        else:
            make = True
            l[j+1] = k
if make:
    print('Sorted List by insertion method : ',l)


