sexo = str(input('Informe o seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Informe o seu Sexo [M/F]: ')).strip().upper()[0]
print('O sexo {} foi registrado com sucesso.'.format(sexo))