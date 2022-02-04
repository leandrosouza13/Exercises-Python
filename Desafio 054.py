from datetime import date
atual = (date.today().year)
totmaior = 0 #COntador
totmenor = 0
for c in range (0,7):
    nascimento = int(input('Digite o ano de nascimento da {}° Pessoa: '.format(c+1)))
    idade = atual-nascimento
    if idade > 21:
        totmaior += 1 #Contador
    else:
        totmenor += 1
print('Ao todo temos {} pessoas maiores de idade\nE também temos {} pessoas menores de idade'.format(totmaior,totmenor))