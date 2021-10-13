cont = -1
soma = 0
while True:
    n = int(input('Digite um número [999 para PARAR]: '))
    cont += 1
    if n == 999:
        break
    soma += n
print(f'Digitou {cont} números e a sua soma foi {soma}.')
