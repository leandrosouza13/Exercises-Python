número = int(input('Digite o número:'))
total = 0
for c in range (1, número+1,1):
    if número % c == 0:
        print('\033[33m', end=" ")
        total = total + 1
    else:
        print('\033[31m',end=" ")
    print('{}'.format(c), end= ' - ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(número,total))
if total == 2:
    print('\nE por isso ele é PRIMO.')
else:
    print('\nE por isso ele NÃO É PRIMO.')
