from time import sleep
v = float(input('Qual a velocidade do carro no momento da leitura?')) #usuário irá digitar a velocidade do carro
print('Ok, irei verificar a sua velocidade!')
sleep(3) # tempo de delay para pensar
if v<=80: # Se a velocidade for 80 ou MENOR imprime a informação abaixo
    print('Pronto, tenha um bom dia e continue dirigindo com segurança!')
else: # Se a velocidade não for 80 imprime a informação abaixo
    print('MULTADO, você excedeu o limite da via que é 80 km/h\nVocê estava a {:.0f} km/h, por isso, será multado em R${:.0f},00.'.format(v,(v - 80) * 7))
