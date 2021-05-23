from datetime import date
# Usando datetime para calcular data de nascimento
datat = date.today().year
print(datat)
while True: # While com o programa, para fazê-lo repetir
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
    if datat - dicion['anonasc'] >= 18: # Validação de idade
        dicion['idad'] =  datat - dicion['anonasc'] # Movendo a idade para uma variável, para uso a seguir
        if dicion['ctps'] != 0: # Validação de CTPS
            dicion['anocontrat'] = int(input('Insira a data de contratação: '))
            dicion['sal'] = float(input('Insira o salário: ').strip().replace(',','.'))
            apost = (dicion['anocontrat'] + 35) - dicion['anonasc']
            print(f'Você irá aposentar com {apost} anos.')
    ch = str(input('Deseja parar o programa?[Sim/Não] ').upper().strip()[0])
    if ch == 'S': 
        break