a = str(input('Digite o seu nome completo: ')).strip()
b = a.split()
print('Muito Prazer em te conhecer!\nO seu primeiro nome é {}\nO seu ultimo nome é {}'.format(b[0].title(),b[len(b)-1].title()))
