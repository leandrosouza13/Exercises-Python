l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
r = int(input('Rendimento da tinta por m²:'))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede você irá precisar de {}L de tinta.'.format(l, a, (l*a), ((l*a)/r)))
