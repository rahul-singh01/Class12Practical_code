# calculating highest common factor

a = int(input('Enter the first no.= '))
b = int(input('Enter the second no.= '))

# by iteration method

while True:
    print(a%b)
    break

# by recursion method

def hcf(a,b):
    if b == 0:
        return a
    else:
        return hcf(b , a%b)
print('recursion', hcf(b , a%b))
