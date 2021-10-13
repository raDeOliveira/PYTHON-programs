def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} marcou {gol} golos no campeonato. ')




#programa principal
n = str(input('Nome jogador: '))
g = str(input('Quantos golos: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
