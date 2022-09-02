# Bar Chart Graph
import matplotlib.pyplot as plt

list1 = ['Physics','Chemistry','Math','English','Computer Sci. ','Phy.Edu']
list2 = []

a = int(input('Enter the marks Obtained in Physics: '))
b = int(input('Enter the marks Obtained in Chemistry: '))
c = int(input('Enter the marks Obtained in Math: '))
d = int(input('Enter the marks Obtained in English: '))
e = int(input('Enter the marks Obtained in Computer Science: '))
f = int(input('Enter the marks Obtained in Physical Education: '))

if a<100 and b<100 and c<100 and d<100 and e<100 and f<100 :
    list2.append(a)
    list2.append(b)
    list2.append(c)
    list2.append(d)
    list2.append(e)
    list2.append(f)
else:
    print('Select Value lower than 100')

marks = float((a+b+c+d+e+f)/6)

plt.bar(list1,list2)
plt.xlabel('Marks')
plt.ylabel('Subject')
plt.title(f'percentage: {marks} %')
plt.show()



