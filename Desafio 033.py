n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: ')) #Se a varialvel n1 for menor que n2 e n3 logo ele é o menor
if n1<n2 and n1<n3:
    print('{} é o menor valor'.format(n1))
if n2<n1 and n2<n3:
    print('{} é o menor valor'.format(n2))
if n3<n1 and n3<n2:
    print('{} é o menor valor'.format(n3))
#Verificando qual é o maior
if n1>n2 and n1>n3:
    print('{} é o maior valor'.format(n1))
if n2>n1 and n2>n3:
    print('{} é o maior valor'.format(n2))
if n3>n1 and n3>n2:
    print('{} é o maior valor'.format(n3))
