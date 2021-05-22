def mesPorExtenso(dd,mm,aaaa):
    mmL = ['','Janeiro','Fevereiro','Março', 'Abril',
    'Maio','Junho','Julho','Agosto','Setembro','Outubro',
    'Novembro', 'Dezembro']
    if aaaa > 0:
        if aaaa % 4 == 0 or aaaa % 400 == 0:
            if mm == 2:
                if dd <= 29:
                    return dd,mmL[mm],aaaa
                else:
                    return 'Data inválida.'
            
        if mm == 4 or mm == 6 or mm == 9 or mm == 11:
            if dd <= 30 and dd > 0:
                return dd,mmL[mm],aaaa
            else:
                return 'Data inválida.'
        elif dd <= 31 and dd > 0:
            return dd,mmL[mm],aaaa
        else:
            return 'Data inválida.'
    else:
        return 'Data inválida.'

dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))
print(f'Data inserida por extenso (apenas o mês) e validada: {mesPorExtenso(dia,mes,ano)}')
