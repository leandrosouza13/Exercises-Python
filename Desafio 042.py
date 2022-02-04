a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b:
    print('Os segmentos acima PODEM FORMAR um triângulo ',end='')#coloca-se end para demonstrar que não terá enter no final da frase
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    elif a==b != c or a==c !=b or c == b != a :
        print('Isósceles')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
