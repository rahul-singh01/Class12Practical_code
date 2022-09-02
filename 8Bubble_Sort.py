
# Bubble sort 

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

    def bubble_sort(l):

        indexing = len(l) - 1
        sort = False

        while not sort:
            sort = True

            for i in range(0 , indexing):

                if l[i] > l[i+1]:
                    sort = False
                    
                    l[i] , l[i+1] = l[i+1], l[i]
        return(l)

    print(bubble_sort(l))
            





 




