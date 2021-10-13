print('-' * 30)
r1 = float(input('Digite o comp. da primeira reta: '))
r2 = float(input('Digite o comp. da segunda reta: '))
r3 = float(input('Digite o comp. da terceira reta: '))
print('-' * 30)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma triângulo')
else:
    print('Não forma triângulo')
