dados = dict()
golos = list()
equipa = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
    golos.clear()
    for c in range(1, partidas+1):
        golos.append(int(input(f'   Quantos golos na partida {c}? ')))
    dados['golos'] = golos[:]
    dados['total'] = sum(golos)
    equipa.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro!Digite apenas S ou N. ')
    if resp == 'N':
        break
print('-=' * 20)
print('cod  ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(equipa):
    print(f'{k:<4} ', end='')
    for v in v.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(equipa):
        print(f'Erro! Não existe jogador com código {busca}! ')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {equipa[busca]["nome"]}: ')
        for i, g in enumerate(equipa[busca]['golos']):
            print(f'    No jogo {i+1} fez {g} golos')
    print('-' * 40)