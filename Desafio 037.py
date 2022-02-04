n1 = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[1] Para BINARIO\n[2] Para OCTAL\n[3] para HEXADECIMAL')
n2 = int(input('Sua opção: '))
if n2 == 1:#Se o usuario escolher o numero 1
    r = bin(n1)[2:]#Técnica de fatiamento de string[2:]
    s = 'binária'
    print('O número {} convertido para a base {} fica {}'.format(n1,s,r))
elif n2 == 2:
    r = oct(n1)[2:]
    s = 'octal'
    print('O número {} convertido para a base {} fica {}'.format(n1,s,r))
elif n2 == 3:
    r = hex(n1)[2:]
    s = 'hexadecimal'
    print('O número {} convertido para a base {} fica {}'.format(n1,s,r))
else:
    print('opção invalida, tente novamente.')