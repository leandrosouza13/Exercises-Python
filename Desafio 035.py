print('=-='*15)
print('Analisador de triângulos')
print('=-='*15)
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')