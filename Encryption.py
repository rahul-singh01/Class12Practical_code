alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,abcdefghijklmnopqrstuvwxyz,0123456789,`~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'
num = '123456789'
code = "Nds3qz =Biqijru|lbr"

def decode(code):
    key = '3=i|^{`Spr'
    final = ''
    key_index = 0
    alternate = 0
    for j, i in enumerate(code):
        
        if j != 0 and j == int(key[0]) + key_index*int(key[0]) + key_index:
            key_index += 1
            continue

        if i not in alpha:
            final += i
            continue

        if i == ' ':
            final += ' '
            continue

        index = alpha.index(i)

        if (index == len(alpha) - 1) and (alternate%2==1):
            change = 'A'
        else:
            if alternate%2==1:
                change = alpha[index + 1]
            else:
                change = alpha[index - 1]
            
        final += change

        alternate += 1

    return final

print(decode(code))