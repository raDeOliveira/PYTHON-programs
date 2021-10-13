valores = []
maior = 0
menor = 0
'''for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont} : ')))
print(f'Você digitou os valores {valores}.')
print('='*30)
print(f'\033[31mA chave ordenada corresponde a {sorted(valores)}\033[m')

print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(cont)}.')
print(f'O menor valor digitado foi {min(valores)} na posição .')'''
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('=-'*25)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições.', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')