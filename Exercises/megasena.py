from random import randint
import time
lista = list()
jogos = list()
print('-'*30)
print('         JOGA MEGA SENA          ')
print('-'*30)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO OS {num} JOGOS! ', '-=' * 3)
tot = 1
while tot <= num:
    cont = 0
    while True:
        computador = randint(1, 60)
        if computador not in lista:
            lista.append(computador)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(0.5)
print('=' * 7, 'BOA SORTE!!', '=' * 7)