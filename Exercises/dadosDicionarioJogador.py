dados = dict()
golos = list()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
for c in range(1, partidas+1):
    golos.append(int(input(f'Quantos golos na partida {c}? ')))
    dados['golos'] = golos[:]
    dados['total'] = sum(golos)
print('-=' * 20)
print(dados)
print('-=' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor de {v}')
print('-=' * 20)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados["golos"]):
    print(f'    => Na partida {i+1}, fez {v}')
print(f'Foi um total de {dados["total"]}')
