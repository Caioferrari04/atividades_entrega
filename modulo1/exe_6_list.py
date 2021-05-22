cond = 0
i = 0
v1 = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?',
'Devia para a vítima?','Já trabalhou com a vítima?']
for i in v1:
    r = (input(i)).lower()
    if r == 'sim':
        cond +=1


print(cond)
if cond < 2:
    print('Inocente!')
elif cond >= 2 and cond < 3:
    print('Suspeito!')
elif cond >= 3 and cond <=4:
    print('Cúmplice!')
elif cond == 5:
    print('ASSASSINO!!!')
