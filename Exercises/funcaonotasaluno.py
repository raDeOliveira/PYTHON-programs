def notas(* n, sit=False):
    '''
    -> função para analisar notas e situações de varios alunos
    :param n: uma ou mais notas(aceita varias)
    :param sit: valor opcional, indicando se deve ou nao mostar a situação
    :return:dicionário com varias informações dos alunos
    '''
    r = dict()
    r['total'] = len(n)
    r['nota maior'] = max(n)
    r['nota menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >=7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['media'] = 'MÁ'
    return r


#programa principal
resp = notas(3, 5, 6, 10, sit=True)
print(resp)