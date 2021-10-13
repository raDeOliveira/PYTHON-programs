def fatorial(n, show=False):
    '''
    -> calcula o fatorial de um número
    :param n: num a ser calculado
    :param show: mostra a conta
    :return: retorna o resultado
    docString por RASO
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f


print(fatorial(5))
print(fatorial(5, show=True))