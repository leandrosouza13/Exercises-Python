a = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase'.format(a.count('a')))
print('A primeira letra A apareceu na posição {}'.format(a.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(a.rfind('a')+1))
