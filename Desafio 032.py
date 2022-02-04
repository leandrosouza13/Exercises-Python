from datetime import date #Modulo para trabalhar com datas
a = int(input('Digite o ano que você quer analisar\nColoque 0 para analisar o ano atual: '))
if a == 0: #Se a varialvel A for igual a zero roda a função date
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0: #Se a varialvel A for divisivel por 4 e o resto da divisão for zero divizivel por 100 e resto diferente de zero ou divisivel por 100 e resto igual a zero
    print('O ano {} é BISSEXTO.'.format(a))
else:
    print('O ano {} não é BISSEXTO.'.format(a))

