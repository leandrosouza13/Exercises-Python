n1 = float(input('Digite uma Distância em metros:'))
print('A medida {}m Corresponde a:\n{}km\n{:.2f}hm\n{:.1f}dam\n{}cm\n{}mm'.format(n1, (n1/1000), (n1/100), (n1/10), (n1*100), (n1*1000)))
