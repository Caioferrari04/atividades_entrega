def funcion(aeiOu,coNt1,ret=''):
    ret = aeiOu
    alf = ['A','E','I','O','U'] # Lista com alfabeto, usada para substituir vogais
    print(ret)
    for i in aeiOu: # For para contar vogais da entrada
        if i in 'AEIOU':
            coNt1 += 1
    for i in alf: # For para substituir vogais, usando a lista como base do for e replace
        ret = ret.replace(i,'')
    # Retorno com as informações.
    return f'A frase "{aeiOu}" tem {coNt1} vogais, se as retirarmos: {ret}.\nForam retiradas {coNt1} letras.'
    


aeiou = str(input('Insira uma frase: ').upper())
cont1 = 0
print(f'{funcion(aeiou,cont1)}')
