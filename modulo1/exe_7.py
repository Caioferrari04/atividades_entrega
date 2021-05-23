temp = list() # lista temporária, usada pra guardar input do usuário
par = list()
impar = list() 
lista = par,impar # movendo listas par e impar para Lista

for i in range(0,7): # Entrada do usuário
    temp.append(int(input('Insira um número: ')))
for i in temp: # Validação de par/impar
    if i % 2 == 0:
        lista[0].append(i)
    else:
        lista[1].append(i)

# Organizando as listas em ordem crescente
par.sort() 
impar.sort()

print(f'Resultado: {lista}')