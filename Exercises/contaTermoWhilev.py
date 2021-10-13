primeiro = int(input('Qual é o primeiro termo: '))
razao = int(input('Qual é a razão? '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais!= 0:
    total += mais
    while cont <= total:
        print('{}-> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA.')
    mais = int(input('Quer ver mais quantos termos? '))
print('FIM!')
