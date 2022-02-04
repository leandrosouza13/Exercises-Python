from datetime import date
print('[M] Masculino\n[F] Feminino')
v1 = str(input('Digite M ou F: '))
m1 = v1.upper()
ano = date.today().year

if m1 == 'M':
    n1 = int(input('Digite o ano de nascimento: '))
    if ano - n1 < 18:
        n2 = ((ano - n1) - 18)*-1
        print('ainda faltam {} anos para o seu alistamento,\nseu alistamento será em {}.'.format(n2,ano+n2))
    elif ano - n1 > 18:
        n3 = (ano - n1) - 18
        print('Você deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(n3,ano-n3))
    elif ano - n1 == 18:
        n4 = (ano - n1) - 18
        print('Quem nasceu em {} tem exatamente {} anos.\nVocê deve ser alistar IMEDIATAMENTE'.format(n1,ano-n1))
elif m1 == 'F':
    print('O alistamento Militar é obrigatório apenas para HOMENS a partir de 18 anos')
else:
    print('ERRO, TENTE NOVAMENTE!')