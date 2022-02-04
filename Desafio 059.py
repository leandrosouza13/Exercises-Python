from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opc = int(input('>>>>> Qual é a sua opção? '))
    if opc == 1:
        print('A soma entre {} + {} é {}'.format(num1, num2, num1 + num2))
    elif opc == 2:
        print('A multiplicação entre {} x {} é {}'.format(num1, num2, num1 * num2))
    elif opc == 3:
        if num1 > num2:
            print('O maior número entre {} e {} é {}'.format(num1, num2, num1))
        if num1 < num2:
            print('O maior número entre {} e {} é {}'.format(num1, num2, num2))
    elif opc == 4:
        print('Digite novos números:')
        num1 = int(input('Digite o 1º novo número: '))
        num2 = int(input('Digite o 2º novo número: '))
    elif opc > 5:
        print('Opção inválida, tente novamente.')
    sleep(3)
print('Finalizando')
sleep(3)