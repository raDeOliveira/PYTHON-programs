nome = str(input('Qual é o seu nome? '))
if nome == 'Rúben':
    print('Que nome bonito!')
elif nome == 'joao' or nome == 'ana' or nome == 'paula':
    print('Nomes diferentes.')
elif nome in 'pedro jessica sandra':
    print('Bem normal')
else:
    print('Ahhhhh')
print('Tenha um bom dia, {}'.format(nome))