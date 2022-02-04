soma = 0 #Acumulador
cont = 0 #contador
for c in range (1,501,2):
    if c % 3 == 0:
        print(c,end = ',')
        soma = soma + c
        cont = cont + 1
print('\nA soma de todos os {} valores solicitados é {}.'.format(cont,soma))