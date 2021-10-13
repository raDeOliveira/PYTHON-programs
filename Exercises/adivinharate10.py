import random
from time import sleep
num = random.randint(0, 5)
'''n = 0
cont = 0
while n != num:
    num = random.randint(0, 5)  # - faz o computador pensar
    n = int(input('Tente adivinhar o número entre 0 a 5: ')) # - jogador tenta adivinhar
    print('PROCESSANDO RESULTADOS...')
    sleep(1)
    print('\n')
    n = n
    cont += 1
    if n == num:
        print()
        print('ACERTOU!! O número escolhido foi {}!'.format(num))
        print('Precisou de {}x tentativas para acertar no número escolhido.'.format(cont))
    else:
        print()
        print('ERRADO! Número escolhido foi {}, e não {}!'.format(num, n))'''
computador = random.randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais para cima...')
        if jogador > computador:
            print('Mais para baixo...')
print('Acertou!! O número escolhido pelo computador foi o \033[31m{}\033[m'.format(computador))
print('Foram necessários {} palpites'.format(palpites))
