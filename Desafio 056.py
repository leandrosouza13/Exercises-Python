acomuladoridade = 0
contadorm = 0
maioridadehomem = 0
nomevelho = '' #Variável para indicar o nome da pessoa mais velha através da variavel nome.
totmulher20 = 0
for pessoas in range (1, 5):
    nome = str(input('Digite o nome da {}°Pessoa: '.format(pessoas)))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [ M ] ou [ F ]: ')).upper()
    acomuladoridade += idade
    if pessoas == 1 and sexo == 'M':
        maioridadehomem = idade #por aqui
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome #até aqui
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
print('A média das idades do grupo é: {:.2f}\nO homem mais velho tem {} anos e se chama {}'.format(acomuladoridade/4,maioridadehomem,nomevelho))
print('Ao todo tem {} mulheres com menos de 20 anos'.format(totmulher20))
