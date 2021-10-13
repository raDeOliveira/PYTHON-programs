frase = str(input('Digite uma frase para analisar: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    from time import sleep
    print('\033[32mANALISANDO OS DADOS... \033[m')
    sleep(2)
    print('Temos palíndromo')
else:
    from time import sleep
    print('\033[32mANALISANDO OS DADOS... \033[m')
    sleep(2)
    print('Não temos palíndromo')
print(junto, inverso)
