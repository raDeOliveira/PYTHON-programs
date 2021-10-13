palavras = ('Carro', 'Casa', 'escola', 'treinar', 'escolher', 'computador', 'fiambre',
            'queijo', 'ovo', 'salsicha', 'jogada', 'filme', 'furadeira', 'brincar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')