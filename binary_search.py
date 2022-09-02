import time

# sorting starts here...

l = []
x = int(input("how many attempts = "))
for i in range(x):
    a = int(input(f'enter number{x-i} = '))
    l.append(a)

def main():
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i] , l[i+1] = l[i+1] , l[i]
        else:
            pass

for i in range(x):
    main()

print(l)
print("all numbers are allocated.. and sorted...")


# binary search starts here...

key = int(input('enter the number you want to search in list = '))
start = time.time()
i = 0
j = len(l)-1
cond = False
while i <= j and not cond:
    mid = (i+j) // 2

    if key == l[mid]:
        cond = True
        pos = mid+1

    elif key > l[mid]:
        i = mid+1

    else:
        j = mid - 1
if cond == True:
    print('no. found at ',pos)
else:
    print('no. not found at ')
end = time.time()

print('binary search executed in ', end - start , ' seconds')



