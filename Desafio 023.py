a = int(input('informe um número: '))
m = a // 1000 % 10
c = a // 100 % 10
d = a // 10 % 10
u = a // 1 % 10
print('analisando o número {}'.format(a))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
