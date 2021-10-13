dados = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 20)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    resp2 = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))
    if resp2 == 999:
        print('FINALIZANDO...')
        break
    if resp2 <= len(dados) - 1:
        print(f'Notas de {dados[resp2][0]} são {dados[resp2][1]}')
