from random import randint
from operator import itemgetter
from time import sleep
jogo = {'Jogador 1:': randint(1, 6),
        'Jogador 2:': randint(1, 6),
        'Jogador 3:': randint(1, 6),
        'Jogador 4:': randint(1, 6)}
ranking = []
print('   \033[4mValores sorteados:\033[m ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.8)
print('-=' * 15)
print('  == \033[31mRanking dos jogadores\033[m ==   ')
print('-=' * 15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
