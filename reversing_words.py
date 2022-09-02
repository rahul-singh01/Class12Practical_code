# recursion and iteration works the same way the main difference between them is that, Iteration is a loop 
# like for and while , but recursion is also a loop but it runs on functions calls...
# iteration takes more space in code but takes less memory
# recursion takes less space in code but take more memory allocations.


# by iteration method
s =''
a = 'hi am rahul singh'
for i in range(len(a)-1,-1,-1):
    print(a[i], end='')

# by recursion method

def rev(a):
    if len(a) == 0:
        return a
    else:
        return rev(a[1:]) + a[0]
print('\nrecursion = ',rev(a))
