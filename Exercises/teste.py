maior = 0
menor = 0

peso = float(input('Digite o {}º peso: '))
if peso == 1:
    maior = peso
    menor = peso
else:
    if peso > maior:
         maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
