frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a", apareçe {}x veze(s) na sua frase.'.format(frase.count('A')))
print('A letra "a" apareçe pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "a" apareçe pela última vez na posição {}'.format(frase.rfind('A')+1))