from time import sleep
print('='*11,'Lojas Souza','='*11)
valor = float(input('Digite o preço das suas compras: R$' ))
print('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cartão de débito\n[ 2 ] à vista cartão de crédito\n'
      '[ 3 ] 2x no cartão de crédito\n[ 4 ] 3x ou mais no cartão de crédito')
p = int(input('Digite a opção desejada para o pagamento: '))
print('calculando valor!')
sleep(1)
if p == 1:
    n1 = valor - (valor/100*(10))
    print('Você teve um desconto de 10% por ter escolhido essa opção.\nSuas compras eram no valor de R${:.0f},00, com desconto irão ficar em RS{:.0f},00.'.format(valor,n1))
elif p == 2:
    n2 = valor - (valor/100*(5))
    print('Você teve um desconto de 5% por ter escolhido essa opção.\nSuas compras eram no valor de R${:.0f},00, com desconto irão ficar em R${:.0f},00.'.format(valor,n2))
elif p == 3:
    n3 = (valor / 2)
    print('Escolhendo essa opção, você irá parcelar as suas compras em até 2x (duas vezes) sem juros no cartão de crédito.\n'
          'Sua compra total é no valor de R${:.0f},00. As parcelas irão ficar em 2x de R${:.0f},00.'.format(valor,n3))
elif p == 4:
    parcelas = int(input('Digite o número de parcelas:'))
    print('Calculando valor! aguarde alguns segundos.')
    sleep(3)
    if parcelas >=3 and parcelas <=10:
        juros = valor + (valor/100*(20))
        n4 = (juros / parcelas)
        print('Escolhendo essa opção, você irá parcelar as suas compras em até 12x (Doze vezes) com juros no cartão de crédito.\n'
          'Sua compra era de {:.0f},00\n'
          'Com o juros o valor total será de {:.0f},00, e as parcelas irão ficar em {:.0f} vezes de R${:.0f},00.'.format(valor,juros,parcelas,n4))
    else:
        print('Nesta opção parcelamos de 3x a 10x com juros.\nCaso você queira parcelar em até 3x retorne ao menu e digite a opção ''3\nOu tente novamente e digite um número de parcelas que esteja entre 3x e 10x')
else:
    print('Opção inválida, TENTE NOVAMENTE!')