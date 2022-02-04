#pedir o peso para o usuário
peso = float(input('Qual é o seu peso? (Kg)'))
#pedir a altura
altura = float(input('Qual é a sua altura? (m)'))
#calculo imc
imc = peso / (altura * altura)
#mostrando status do usuario de acordo com o IMC
if imc <= 18.5:
    print('Seu IMC é {:.1f}, você está magro demais.'.format(imc))
elif imc >18.6 and imc <= 25:
    print('PARABÉNS, seu IMC é {:.1f} e você está no peso idel, continue assim.'.format(imc))
elif imc >25.1 and imc <= 30:
    print('Cuidado, o seu IMC está em {:.1f}, você está com sobrepeso.'.format(imc))
elif imc >30.1 and imc <=40:
    print('Você está com o IMC em {:.1f}, você está OBESO.'.format(imc))
else:
    print('Você tem o IMC de {:.1f}, você é OBESO MÓRBIDO, FAÇA UMA DIETA AGORA OU IRÁ MORRER.'.format(imc))