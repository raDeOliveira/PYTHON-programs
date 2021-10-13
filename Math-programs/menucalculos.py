r = 0
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
while r != 5:
    print('''
    [ 1 ] - SOMAR
    [ 2 ] - MULTIPLICAR
    [ 3 ] - MAIOR
    [ 4 ] - NOVOS NÚMEROS
    [ 5 ] - SAIR DO PROGRAMA''')
    r = int(input('»»»»» Escolha uma opção:'))
    if r == 1:
        soma = n1 + n2
        print('A soma entre {}+{} é de {}'.format(n1, n2, soma))
    elif r == 2:
        multi = n1 * n2
        print('A entre {}*{} é de {:.2f}'.format(n1, n2, multi))
    elif r == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor é {}'.format(maior))
        elif n1 < n2:
            print('O maior valor é {}'.format(maior))
            maior = n2
        else:
            print('Os valores digitados são iguais!')
    elif r == 4:
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
    elif r == 5:
        from time import sleep
        print('\033[32mFINALIZANDO...\033[m')
        sleep(2)
    else:
        print('Opção inválida! Tente novamente.')
    print('->'*20)
print('FIM!!')
