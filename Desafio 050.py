soma = 0
cont = 0
soma1 = 0
cont1 = 0
for c in range (1,7):
    numero = int(input('Digite o {}° valor: '.format(c)))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1
print('Você informou {} números\nEntre eles tem {} números PARES e a soma entre eles é {}.'.format(c, cont,soma))
