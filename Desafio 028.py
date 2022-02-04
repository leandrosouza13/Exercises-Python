from random import randint
from time import sleep
print('=--='*15)
print('Vou pensar em um número entre 0 e 3. tente adivinhar...')
print('=--='*15)
n1 = int(input('Em que número eu pensei?'))
print('Processando')
sleep(2)
n2 = randint(0,3)
if n1 == n2:
    print('PARABENS, eu também escolhi o número {}, você conseguiu me vencer!!!!!!!!!!'.format(n2))
if n1 != n2:
    print('VOCÊ PERDEU, Eu pensei no numero {} e não no {}!'.format(n2,n1))
