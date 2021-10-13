sal = float(input('Qual é o seu salário? '))
'''if sal > 1250:
    nsal = sal + (sal * 15 / 100)
    print('Seu novo salário com um aumento de 10% é de {}'.format(nsal))
if sal <= 1250:
    nsal = sal + (sal * 10 / 100)
    print('O seu novo salário com um aumento de 15% é {} €!'.format(nsal))'''

if sal <= 1250:
    nsal = sal + (sal * 15 / 100)
else:
    nsal = sal + (sal * 10 / 100)
print('O salário de {}, com o aumento será agora de {}'.format(sal, nsal))