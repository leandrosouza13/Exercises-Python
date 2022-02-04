casa = float(input('Qual é o valor da casa?R$ '))
salario = float(input('Qual é o seu salário?R$ '))
anos = int(input('Em quantos anos você quer pagar o empréstimo? '))
valor = casa / (anos*12)
salario2 = ((salario * 30) / 100)
if valor <= salario2:
    b = 'APROVADO'
elif valor > salario2:
    b =  'Reprovado'
print('O valor da casa é de R${:.0f},00, para pagar em {} anos, com isso a prestação será de R${:.0f},00 e você possui um salário de R${:.0f},00\n'
      'com base nessas informações você teve o emprestimo {}'.format(casa,anos,valor,salario,b))