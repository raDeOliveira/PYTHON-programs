dados = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    dados.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo foram registadas {len(dados)} pessoas. ')
print(f'O peso maior foi de {maior}Kg. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
