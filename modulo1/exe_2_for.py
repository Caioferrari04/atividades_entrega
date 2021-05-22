aeiou = str(input('Insira uma frase: ').upper())
cont1 = 0

for i in aeiou:
    if i in 'AEIOU':
        cont1 += 1
print(f'Vogais apareceram na sua frase {cont1} vezes.')
print(f'Frase digitada sem vogais:')
for i in aeiou:
    if i in 'AEIOU':
        print(end='')
    else:
        print(i, end='')
