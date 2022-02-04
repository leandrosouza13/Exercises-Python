a = str(input('Digite o seu nome completo: ')).strip()
b = a.split()
print('Analisando o seu nome...')
print('O seu nome em MAIÚSCULAS é: {}'.format(a.upper()))
print('O seu nome em minúsculas é: {}'.format(a.lower()))
print('Seu nome tem ao todo {} letras'.format(len(a)-a.count(' ')))#função len para saber quantos caracteres tem a frase - quantidade de espaços utilizando a funcão count#
print('Seu primeiro nome é {} e ele tem {} letras'.format(b[0],len(b[0])))
