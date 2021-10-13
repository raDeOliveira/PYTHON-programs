'''import math
ca = float(input('Dado o seguinte triângulo, indique a medida do cateto adjacente: '))
co = float(input('Agora, indique a medida do cateto oposto: '))
h = (pow(ca, 2) + pow(co, 2))  ** (1/2)
print('O valor da hipotnusa deste triângulo é de {:.2f}'.format(h))'''

'''import math
co= float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(h))'''

from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print('A hipotenusa é {:.2f}'.format(hypot(co, ca)))