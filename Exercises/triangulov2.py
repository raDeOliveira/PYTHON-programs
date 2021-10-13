r1 = float(input('Compr. reta 1: '))
r2 = float(input('Compr. reta 2: '))
r3 = float(input('Compr. reta 3: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('É possível formar um triângulo.')
    if r1 == r2 == r3:
        print('Triângulo EQUILÁTERO, tem todos os lados iguais.')
    elif r1 != r2 != r3 != r1:
        print('Triângulo ESCALENO, todos os seus lados sao diferentes')
    else:
        print('Triângulo ISÓSCELES, tem dois lados iguais')

else:
    print('Não é possível formar um triângulo.')

'''if r1 == r2 and r1 == r3 and r2 == r3:
    print('Triângulo EQUILÁTERO, tem todos os lados iguais.')
elif r1 == r2 and r3 != r1 and r3 != r2:
    print('Triângulo ISÓSCELES, tem dois lados iguais')
elif r1 != r2 and r2 != r3 and r1 != r3:
    print('Triângulo ESCALENO, todos os seus lados sao diferentes')
'''