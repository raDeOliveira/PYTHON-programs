from datetime import datetime
print('-'*25)
print('Registo de Pessoa')
print('-'*25)
'''tot20 = tot18 = tothomem = totmulher = 0
atual = datetime.today().year
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade <= 20:
        tot20 += 1
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F':
        totmulher += 1
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Estão registados {tothomem} homem(s).')
print(f'No total de {totmulher} mulher(es)registadas, {tot20} mulher(es) têm menos de 20 anos.')'''
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade <= 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homem(ns) registados. ')
print(f'E temos {totM20} mulher(es) com menos de 20 anos.')
