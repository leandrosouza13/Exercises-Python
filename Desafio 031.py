d = float(input('Digite a distancia da viagem: ')) #usuário digita a km da viagem
print('Você está prestes a começar uma viagem de {:.0f} km'.format(d))
if d <= 200: #Se a vigem for menor ou igual a 200km a corrida será por 0,50 centavos por km
    print('O valor desta viagem será de R$ {:.0f},00.'.format(d*0.50))
    print('tenha um ótimo dia')
else:#se não a corrida será por 0,45 por km
    print('O valor desta viagem será de R$ {:.0f},00.\ntenha um ótimo dia.'.format(d*0.45))
