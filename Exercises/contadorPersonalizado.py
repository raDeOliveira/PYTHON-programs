from time import sleep
def contador(i, f, p):
        if p < 0:
            p *= -1
        if p == 0:
            p = 1
        print('-=' * 30)
        print(f'Contagem de {i} ate {f} de {p} em {p}')
        sleep(2)

        cont = i
        if i < f:
            while cont <= f:
                print(f'{cont} ', end='')
                cont += p
                sleep(0.2)
            print('FIM!!')
        else:
            while cont >= f:
                print(f'{cont} ', end='')
                cont -= p
                sleep(0.2)
            print('FIM!!')
            print('-=' * 30)


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)