'''import math
ang = float(input('Digite um ângulo qualquer ºC: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
import emoji
print('='*40)
print('O sen desse ângulo é {:.2f}, '
      '\nO cosseno desse mesmo ângulo é {:.2f}, \nenquanto a tangente será de {:.2f}'.format(sen, cos,tg),
      (emoji.emojize(':white_check_mark:', use_aliases=True)))'''

from math import sin, cos, radians, tan
ang = float(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print('O seno é {:.2f}, \no cosseno é {:.2f}, \ne a tangente é {:.2f}'.format(sen, cos, tg))