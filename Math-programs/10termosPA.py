primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('ACABOU')
