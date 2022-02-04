n1 = 0
cont = 0
acomulador = 0
while n1 != 999:
    if n1 != 999:
        n1 = int(input('Digite um número [ 999 para parar ]: '))
        cont += 1
        if acomulador != 999:
            acomulador += n1
print('Você digitou {} números e a soma deles é {}.'.format(cont,acomulador-999))
