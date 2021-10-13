from datetime import date
ano = int(input('Digite um ano qualquer. Para ano atual prima 0. '))
if ano == 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print()
    print('O ano {} é Bissexto'.format(ano))
else:
    print()
    print('O ano {}, não é Bissexto'.format(ano))
