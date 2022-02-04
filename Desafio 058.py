from random import randint
print('''Sou o seu computador...
Acabei de pensar em um número entre 0 e 10.
Sera que você consegue adivinhar qual foi?''')
palpite = int(input('Qual é o seu palpite? '))
numero = randint(0,10)
cont = 0
while palpite != numero:
    if palpite < numero:
        print('Mais... tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
        cont += 1
    elif palpite > numero:
        print('Menos... tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
        cont += 1
print('Acertou!!!O número que eu pensei foi o {}\nVocê acertou com {} tentativas. Parabéns.'.format(numero,cont+1))
