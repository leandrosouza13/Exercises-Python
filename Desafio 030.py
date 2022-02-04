n1 = int(input('Digite um número qualquer: ')) #usuário digita um número
r = n1 % 2 #calculo que demonstra resto da divisão, neste caso ou resto é 1 ou 0
if r == 0: #Se o resultado da dívisão for igual a zero imprime o resultado par
    print('O número {} é PAR.'.format(n1))
else: #Se não for par imprime o resultado ímpar
    print('O numero {} é ímpar.'.format(n1))
