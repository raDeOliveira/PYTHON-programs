lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso. ')
    else:
        print('Valor duplicado. Não é possível adicionar... ')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
# lista.sort() # também dá assim
print(f'Seus valores ordenados são: {sorted(lista)}') # aqui so fica lista