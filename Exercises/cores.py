a = 'Rúben'
z = 'cores'
'''print('Olá! Prazer em conhecer te {}{}{}'.format('\033[33m', a, '\033[32m \033[m'))

b = 3
c = 5
print('Os valores são \033[32m{} e '
      '\033[35m{}'.format(b, c))'''

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Oi! Tudo em ordem, fase de teste de cores {}{}{} {}'.format(cores['azul'], z, cores['amarelo'], a))