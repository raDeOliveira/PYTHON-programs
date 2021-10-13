print('='*20)
print('{:^20}'.format('BANCO DÁ TUDO!!'))
print('='*20)
valor = int(input('Quanto dinheiro deseja levantar?€ '))
total = valor
nota = 50
totnota = 0
while True:
    if total >= nota:
        total -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'Total de {totnota} notas de {nota}€.')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre!')
