from math import hypot
o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('Digite o comprimento do cateto adjascente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(o,a)))
