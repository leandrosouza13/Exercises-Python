print('--'*30)
print('Sequência de fibonacci')
print('-'*30)
termos = int(input('quantos termos você quer mostrar? '))
print('~'*30)
t1 = 0
t2 = 1
cont = 3
print('{} ¬ {}'.format(t1, t2), end = ' ')
while cont <= termos:
    t3 = t2 + t1
    print('¬ {}'.format(t3), end = '')
    t1 = t2
    t2 = t3
    cont += 1
