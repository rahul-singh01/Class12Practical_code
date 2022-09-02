# calculating power

a = 3
b = 2

# by iteration method 

for i in range(b-1):
    a *= a
print(a)

# by recursion method

def power(a,b):
    if b==0:
        return 1
    else:
        return a * power(a, b-1)
print('recursion = ',power(a,b-1))