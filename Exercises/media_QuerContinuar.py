r = 'S'
quant = media = soma = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média é {:.2f}!'
              '\nO maior valor foi {}, e o menor valor foi {}'.format(quant, media, maior, menor))
print('Fim')
