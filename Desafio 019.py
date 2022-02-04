from random import choice
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
l = [a,b,c,d,]
print('O aluno escolhido é {}'.format(choice(l)))
