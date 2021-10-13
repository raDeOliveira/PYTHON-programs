n = int(input('Digite um número: '))
tot = 0
# percorre contagem ate num inserido
for c in range(1, n + 1):
    # verifica resto divisão pela contagem
    if n % c == 0:
        # se (% = 0), incrementa tot
        tot += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisivel {}x.'.format(n, tot))
if tot == 2:
    print('PRIMO')
else:
    print('NÃO É PRIMO')
