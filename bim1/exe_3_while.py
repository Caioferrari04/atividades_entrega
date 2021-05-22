from random import randint

senha = 'abcde'

entrada = str(input('Insira a senha: '))
numpc = randint(0,11)
cont1 = 0

if entrada == senha:
    print('Bem vindo ao jogo de adivinhações!')
    print('Ou seja... bem vindo ao show dos horrores!')
    print('¬>¬>'*20)
    while True:
        numjog = int(input('Insira a sua aposta: '))
        if numjog == numpc:
            print(f'Parabéns! Você acertou, o número era {numpc}')
            print(f'Foram necessários {cont1} palpites para adivinhar o número correto.')
            break
        if numjog > numpc:
            print('Quase! O número correto é menor!')
        if numjog < numpc:
            print('Quase! O número correto é maior!')
        cont1 += 1
else:
    print('SENHA ERRADA!!!!!!!!!!!!!!!!!!!!!!!!!!')