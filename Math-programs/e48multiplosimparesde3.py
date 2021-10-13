soma = 0
cont = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        soma = soma + c
        cont += 1
print('A soma de todos os {} valores solicitados é \033[31m{}\033[m'.format(cont, soma), end=' ')
