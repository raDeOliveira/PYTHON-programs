'''import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
esc = random.choice(lista)
print('O aluno escolhido para apagar o quadro é {}'.format(esc))'''

from random import choice
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite outro nome: '))
n3 = str(input('Digite um terceiro nome: '))
n4 = str(input('Digite um quarto nome: '))
list = [n1, n2, n3, n4]
esc = choice(list)
print('O aluno escolhido foi : {}'.format(esc))