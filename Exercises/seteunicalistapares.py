'''dados = list() # meu código
for c in range(1, 8):
    dados.append(int(input(f'Digite o {c}º valor: ')))
    pares = list()
    impares = list()
    for c in dados[:]:
        if c % 2 == 0:
            pares.append(c)
        elif c % 2 == 1:
            impares.append(c)
print('-='*30)
print(f'Os valores pares digitados foram {sorted(pares)}')
print(f'Os valores impares digitados foram {sorted(impares)}')'''
dados = [[], []]
valor = 0
for c in range(1 ,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        dados[0].append(valor)
    elif valor % 2 == 1:
        dados[1].append(valor)
print(f'Todos os valores {dados}')
print('-='*30)
print(f'Os PARES são: {sorted(dados[0])}')
print(f'Os IMPARES são: {sorted(dados[1])}')