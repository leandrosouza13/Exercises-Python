from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
print('Você tem {} anos de idade.'.format(idade))
if idade >= 0 and idade <= 9:
    print('Sua classificação é MIRIM')
elif idade >= 10 and idade <= 14:
    print('Sua classificação é INFANTIL.')
elif idade >= 15 and idade <= 19:
    print('Sua Classificação é JÚNIOR.')
elif idade >= 16 and idade <= 25:
    print('Sua classificação é SÊNIOR.')
elif idade > 25:
    print('Sua classificação é MASTER.')
