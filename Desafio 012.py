a = float(input('Qual é o preço do produto? R$ '))
print('O produto que custava R${} reais, na promoção com 5% de desconto passará a custar R${:.2f} reais'.format(a,a-(a*0.05)))
