from datetime import date

datat = date.today().year
print(datat)
while True:
    dicion = {
        'nome': '',
        'anonasc': 0,
        'ctps': 0,
        'idad': 0,
        'anocontrat': 0,
        'sal':0
    }

    dicion['nome'] = str(input('Insira o seu nome: '))
    dicion['anonasc'] = int(input('Insira a sua data de nascimento: '))
    dicion['ctps'] = int(input('Insira sua CTPS: '))
    if datat - dicion['anonasc'] >= 18:
        dicion['idad'] =  datat - dicion['anonasc']
        if dicion['ctps'] != 0:
            dicion['anocontrat'] = int(input('Insira a data de contratação: '))
            dicion['sal'] = float(input('Insira o salário: ').strip().replace(',','.'))
            apost = (dicion['anocontrat'] + 35) - dicion['anonasc']
            print(f'Você irá aposentar com {apost} anos.')
    ch = str(input('Deseja parar o programa?[Sim/Não] ').upper().strip()[0])
    if ch == 'S':
        break