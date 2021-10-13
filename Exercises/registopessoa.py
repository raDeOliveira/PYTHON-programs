from datetime import datetime
lista = dict()
lista['nome'] = str(input('Nome: '))
lista['ano'] = int(input('Ano de nascimento: '))
lista['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
atual = datetime.today().year
idade = atual - lista["ano"]
if lista["ctps"] == 0:
    print('-=' * 15)
    print(f'Nome tem o valor {lista["nome"]}')
    print(f'Idade tem o valor {idade}')
    print(f'CTPS tem o valor de {lista["ctps"]}')
else:
    if lista['ctps'] > 0:
        lista['contrato'] = int(input('Ano de contratação: '))
        lista['salario'] = float(input('Salário €: '))
        lista['reforma'] = lista['contrato'] + 35 - datetime.today().year + idade
        print('-=' * 15)
    for k, v in lista.items():
        print(f'  - {k} tem o valor igual a {v}.')
