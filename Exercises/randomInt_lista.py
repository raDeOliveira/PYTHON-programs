from random import randint
from time import sleep

num = list()
def sorteio(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(1, 6):
        n = randint(1, 10)
        num.append(n)
        print(f'{n} ', end=' ')
        sleep(0.3)
    print('FIM!!')
    print('-' * 50)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma entre os pares da lista {lista} vale {soma}')



#programa principal
sorteio(num)
somapar(num)