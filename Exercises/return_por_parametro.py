def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA! '
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'


#programa principal
ano = int(input('Nasceu em que ano? '))
print(voto(ano))
