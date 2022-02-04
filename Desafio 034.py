n1 = float(input('Digite o salário para descobrir o aumento: R$'))
if n1 <=1250:
    s1 = ((n1*15)/100)+n1
if n1 >1250:
    s1 = ((n1*10)/100)+n1
print('O salário de R${:.2f} teve um aumento e foi para R${:.2f}.\nGaste com moderação'.format(n1,s1))