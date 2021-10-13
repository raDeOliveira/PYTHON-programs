total = menor = totmil = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço €: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi {total:.2f}€.')
print(f'Temos {totmil} produtos que custam mais de 1000€.')
print(f'O produto mais barato foi {barato} que custou {menor}€.')
print('{:^40}'.format('FIM DO PROGRAMA.'))
