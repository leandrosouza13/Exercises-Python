print('Gerador de PA')
print('=-'*10)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
termo = n1
cont = 1
total = 0
n3 = 10
while n3 != 0:
    total = total + n3
    while cont <= total:
        print('{} ¬'.format(termo), end = ' ')
        termo += n2
        cont += 1
    print('PAUSA')
    n3 = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos'.format(total))

