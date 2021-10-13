num = int(input('Digite um número inteiro qualquer: '))
print()
escolha = int(input('Quer converter esse número para que Base?'
                    '\nEscolha uma opção: '
                    '\n\033[35m[1]\033[m - BINÁRIO?'
                    '\n\033[35m[2]\033[m - OCTAL?'
                    '\n\033[35m[3]\033[m - HEXADECIMAL? '))
print()
if escolha == 1:
    print('\033[31m{}\033[m em \033[7;4mBinario\033[m é \033[36m{}: '.format(num, bin(num)[2:]))
elif escolha == 2:
    print('\033[31m{}\033[m em \033[7;4mOctal\033[m é \033[36m{}: '.format(num, oct(num)[2:]))
elif escolha == 3:
    print('\033[31m{}\033[m em \033[7;4mHexadecimal\033[m é \033[36m{}: '.format(num, hex(num)[2:]))
else: print('Opção inválida, tente novamente!')
