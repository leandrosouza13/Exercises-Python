n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print('Parabéns a nota do aluno foi {}.\nAluno APROVADO!'.format(m))
elif m <= 5:
    print('A nota do aluno foi {}.\nprecisa melhorar.\nAluno em RECUPERAÇÃO'.format(m))
elif m > 5 and m < 6.9:
    print('A nota do aluno foi {}.\nEle precisa provar os seus valores.\naluno em RECUPERAÇÃO.'.format(m))
