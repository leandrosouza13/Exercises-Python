maior = 0
menor = 0
#laço de leitura de 5 pessoas
for pessoas in range (1,6):
    #leitura dos pesos
    peso = float(input('Digite o peso da {}° pessoa: '.format(pessoas)))
    #Se for o primeiro dado do laço ele será o maior e o menor.
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        #Se o peso for maior que ele passa a ser o maior peso
        if peso > maior:
            maior = peso
            #Se o peso for menor ele passa a ser o menor peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.0f}Kg\nE o menor peso lido foi de {:.0f}Kg.'.format(maior,menor))
