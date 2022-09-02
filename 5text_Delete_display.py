
# DELETION OF WORD FROM A TEXT FILE.

file = open('tut2.txt','r')
file = file.read().split(' ')

word = input('Enter the word you want to delete: ')

for i in file:
    if word == i:
        file.remove(i)
        
final = ''
for i in file:
    final += i
    final += ' '.join(' ')

print(f'Modified text -- ',final)

with open('tut2.txt', 'w') as f:
    f.write(final)
