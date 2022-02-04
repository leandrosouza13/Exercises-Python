from time import sleep
from random import randint
print('Vamos jogar JO KEN PO?\n[ 1 ] SIM\n[ 2 ] NÃO')
n1 = int(input('Digite 1 para jogar e 2 para não jogar:'))
if n1 == 1:
    print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
    n2 = int(input('Escolha a sua opção:'))
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    n3 = randint(0,2)
    print('-='*12)
    if n3 == 0:
        print('Computador jogou PEDRA')
    elif n3 == 1:
        print('Computador jogou PAPEL')
    elif n3 == 2:
        print('Computador jogou TESOURA')
    if n2 == 0:
        print('Jogador jogou PEDRA')
    elif n2 == 1:
        print('Jogador jogou PAPEL')
    elif n2 == 2:
        print('Jogador jogou TESOURA')
    print('-='*12)
    if n2 == n3:
        print('EMPATE, tente novamente.')
    elif n3 == 0 and n2 == 2 or n3 == 1 and n2 == 0 or n3 == 2 and n2 == 1:
        print('COMPUTADOR VENCEU :(')
    elif n2 == 0 and n3 == 2 or n2 == 1 and n3 == 0 or n2 == 2 and n3 == 1:
        print('JOGADOR VENCEU!!!!!')
    else:
        print('Número inválido, tente novamente!')
elif n1 == 2:
    print('Ok, quando quiser estarei aqui :)')
else:
    print('Número inválido, tente novamente!')
