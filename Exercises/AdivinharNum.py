import random
num = random.randint(0, 5) # - faz o computador pensar
from time import sleep
n = int(input('Adivinhe o número escolhido pelo computador: ')) # - jogador tenta adivinhar
print('PROCESSANDO RESULTADOS...')
sleep(2)
if n == num:
    print()
    print('ACERTOU!! O número escolhido foi {}!'.format(num))
else:
    print()
    print('ERRADO! Número escolhido foi {}, e não {}!'.format(num, n))
