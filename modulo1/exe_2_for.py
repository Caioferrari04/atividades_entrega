aeiou = str(input('Insira uma frase: ').upper())
vogais = ['A','E','I','O','U'] #Essa lista irá ser utilizada para substituir as vogais
cont1 = 0

for i in aeiou:
    if i in 'AEIOU': # Para cada repetição, cheque se "i" é uma vogal
        cont1 += 1 # se sim, +1 no contador.
print(f'Vogais apareceram na sua frase {cont1} vezes.')
print(f'Frase digitada sem vogais:')
for i in vogais:
    aeiou = aeiou.replace(i,'') # Irá substituir todas as vogais do usuário

print(aeiou)
