temp = list()
par = list()
impar = list()
lista = par,impar

for i in range(0,7):
    temp.append(int(input('Insira um número: ')))
for i in temp:
    if i % 2 == 0:
        lista[0].append(i)
    else:
        lista[1].append(i)
        
par.sort()
impar.sort()

print(f'Resultado: {lista}')