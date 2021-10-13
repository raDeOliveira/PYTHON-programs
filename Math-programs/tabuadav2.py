cont = 1
while True:
    num = int(input('Qual a tabuada queres ver? '))
    print()
    if num < 0:# se digitar número negativo programa encerra
        break
    for cont in range(1 , 11):
        multi = num * cont
        print(f'{num}x{cont} = {multi}')
    print('-' * 30)
print('Acabou! Você digitou um número negativo!')
