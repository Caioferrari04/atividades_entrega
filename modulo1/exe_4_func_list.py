def mesPorExtenso(dd,mm,aaaa):
    mmL = ['','Janeiro','Fevereiro','Março', 'Abril',
    'Maio','Junho','Julho','Agosto','Setembro','Outubro',
    'Novembro', 'Dezembro'] # Casa 0 não há nada, para facilitar contagem
    if aaaa > 0: # Verificando se ano não é negativo
        if aaaa % 4 == 0 or aaaa % 400 == 0: # Validação de anos bissextos
            if mm == 2:
                if dd <= 29:
                    return dd,mmL[mm],aaaa
                else:
                    return 'Data inválida.'
            
        if mm == 4 or mm == 6 or mm == 9 or mm == 11: # Validação de meses com 30 dias
            if dd <= 30 and dd > 0:
                return dd,mmL[mm],aaaa
            else:
                return 'Data inválida.'
        elif dd <= 31 and dd > 0: # Validação de dias, de meses com 31 dias
            return dd,mmL[mm],aaaa
        else:
            return 'Data inválida.'
    else:
        return 'Data inválida.'

dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))
print(f'Data inserida por extenso (apenas o mês) e validada: {mesPorExtenso(dia,mes,ano)}')
