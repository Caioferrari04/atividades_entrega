# Desafio: apenas 2 variáveis.

while True:
    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira outro número: '))
    print(f'A soma dos dois números é: {num1+num2}')
    print(f'A multiplicação dos dois números é: {num1*num2}')
    print(f'A divisão inteira deles é: {num1//num2}')
    if num2 > num1:
        print(f'O número {num2} é maior que {num1}')
    else:
        print(f'O número {num1} é maior que {num2}')

    # Se a multiplicação de num2*num1 for maior que 40,
    # sua divisão por inteiro for diferente de 0, faça:
    # Caso tudo seja cumprido, o programa irá dividir o
    # resultado da multiplicação de num1 e num2, e dividir
    # pelo resultado da divisão inteira dos mesmos.
    
    if num2 * num1 > 40 and num1//num2 != 0 and num2//num1 != 0:
        print(f'O resultado é: {((num1*num2))/(num1//num2)}')
    else:
        print('Não foi maior que 40.')
    
