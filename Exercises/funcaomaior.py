from time import sleep
def maior(* num):
    cont = maior = 0
    print('\033[32m-=\033[m' * 20)
    print(f'Analisando os valores passados...')
    for k, v in enumerate(num):
        print(f'\033[32m{v}\033[m. ', end='')
        sleep(0.2)
    print(f'Foram informados {len(num)} valores.')
    print(f'O maior valor informado foi o \033[31m{max(num)}\033[m!!')
'''    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'informados {cont} valores')
    print(f'o maior é {maior}')'''


#programa principal
maior(4, 5, 7, 9, 1, 3)
maior(4, 25, 2)
maior(1, 14)
maior(7)
maior(0)