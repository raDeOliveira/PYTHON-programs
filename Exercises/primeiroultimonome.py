n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Primeiro nome é: {}'.format(nome[0]))
print('Último nome é: {}'.format(nome[len(nome)-1]))
