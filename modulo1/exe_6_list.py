cond = 0 # Contador de suspeita
v1 = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?',
'Devia para a vítima?','Já trabalhou com a vítima?'] 
# Lista com perguntas, usada para diminuir o uso de prints
for i in v1: # Perguntando ao usuário, usando a lista de perguntas
    r = (input(i)).lower() # Resposta do usuário
    if r == 'sim':
        cond +=1 # Se a resposta for sim, adicione ao contador de suspeita


print(cond)
#Verifica se o contador de suspeitas for maior que x numero, e mostra o resultado
if cond < 2:
    print('Inocente!')
elif cond >= 2 and cond < 3:
    print('Suspeito!')
elif cond >= 3 and cond <=4:
    print('Cúmplice!')
elif cond == 5:
    print('ASSASSINO!!!')
