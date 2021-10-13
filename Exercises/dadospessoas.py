lista = list()
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F. ')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 20)
print(f'A) O total de pessoas registadas é {len(lista)}')
media = soma / len(lista)
print(f'B) A media de idades do grupo é de {media:.2f} anos. ')
print(f'C) As mulheres registadas são ', end='')
for p in lista:
    if p['sexo'] in'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média do grupo: ')
print()
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRANDO >>')
