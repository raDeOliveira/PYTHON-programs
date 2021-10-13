preco = float(input('Qual o valor do produto €? '))
desc10 = (preco * 10) /100
desc5 = (preco * 5) /100
juros = (preco * 10) / 100
pagamento = str(input('[1] - Pagar com € ou cheque tem 10% de desconto'   #- outra forma
                  '\n[2] - Pagar com cartão tem 5% de desconto.'
                  '\n[3] - Pagar a 2x no cartão não tem desconto.'
                  '\n[4] - Pagar a 3x no cartão, acumula juros de 20%'
                      '\nEscolha uma opção por favor: '))
if pagamento == '1':
    print('Paga um valor de {}€. Teve um desconto de 10%'.format(preco - desc10))
elif pagamento == '2':
    print('Paga um valor de {}€. Teve um desconto de 5%.'.format(preco - desc5))
elif pagamento == '3':
    print('Pagará o valor normal sem desconto.')
elif pagamento == '4':
    print('Pagará o valor de {}€, acrescido de juros, {}€'.format(preco, juros))
else:
    print()
    print('Tente de novo! ')