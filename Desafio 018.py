import math
v = float(input('Digite o angulo desejado: '))
a = math.radians(v)
print('O ângulo de {:.2f}º tem o SENO de {:.2f}\nO ângulo de {:.2f}º tem o COSSENO de {:.2f}\nO ângulo de {:.2f}º tem a TANGENTE de {:.2f}'.format(v,math.sin(a),v,math.cos(a),v,math.tan(a)))
