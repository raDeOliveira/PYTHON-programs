print('{:=^40}'.format('Lojas Rúben'))
preco = float(input('Preço das compras €? '))
print('''FORMAS DE PAGAMENTO
[1] - Dinheiro/ Cheque
[2] - Com cartão
[3] - 2x com cartão
[4] - 3x ou mais com cartão''')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    total = preco - (preco * 10 /100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será dividida em 2x de {}€'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas vezes? '))
    parcela = total / totalparc
    print('Sua compra sera dividida em {}x de {:.2f}€ com juros'.format(totalparc, parcela))
else:
    total = preco
    print('Opção inválida, tente novamente!!')
print('Sua compra de {}€, vai custar {:.2f}€'.format(preco, total))