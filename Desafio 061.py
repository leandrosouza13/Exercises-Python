print('Gerador de PA')
print('=-'*10)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
termo = n1
cont = 1
while cont <= 10:
    print('{} ¬'.format(termo), end = ' ')
    termo += n2
    cont += 1
print('Fim.')
