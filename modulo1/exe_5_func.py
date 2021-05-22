def funcion(aeiOu,coNt1,ret=''):
    ret = aeiOu
    alf = ['A','E','I','O','U']
    print(ret)
    for i in aeiOu:
        if i in 'AEIOU':
            coNt1 += 1
    for i in alf:
        ret = ret.replace(i,'')

    return f'A frase "{aeiOu}" tem {coNt1} vogais, se as retirarmos: {ret}.\nForam retiradas {coNt1} letras.'
    


aeiou = str(input('Insira uma frase: ').upper())
cont1 = 0
print(f'{funcion(aeiou,cont1)}')
