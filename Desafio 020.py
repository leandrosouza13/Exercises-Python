from random import shuffle
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
l = [a,b,c,d]
shuffle(l)
print('A ordem de apresentação será:\n{}'.format(l))

