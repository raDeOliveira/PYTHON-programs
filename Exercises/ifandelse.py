'''nome = str(input('Qual é o seu nome? ')).upper()
if nome == 'RÚBEN':
    print('Que nome MAIS LINDO tens.')
else:
    print('Nome muito comum')
print('Bom dia {}'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f},'.format(m))
if m >= 6:
    print('Portanto a média foi boa')
else:
    print('Sua média foi baixa')
'''print('Parabéns' if m >= 6 else 'Nota ruim')'''