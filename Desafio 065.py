continuar = 'S' or 'N'
cont = acomulador = maior = menor = 0
while continuar == 'S':
    n1 = int(input('Digite um número: '))
    cont += 1
    acomulador += n1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
média = acomulador / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont,média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
