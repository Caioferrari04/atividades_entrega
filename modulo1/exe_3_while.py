from random import randint

senha = 'abcde'

entrada = str(input('Insira a senha: '))
numpc = randint(0,11) # Geração de números do computador
cont1 = 0

if entrada == senha: # Se a entrada do jogador for igual a senha, permita.
    print('Bem vindo ao jogo de adivinhações!')
    print('Ou seja... bem vindo ao show dos horrores!')
    print('¬>¬>'*20)
    while True: # Enquanto o usuário não acertar, continue.
        numjog = int(input('Insira a sua aposta: ')) # Aposta do jogador
        if numjog == numpc: # Se o usuário acertou, parabenização e terminando o programa.
            print(f'Parabéns! Você acertou, o número era {numpc}')
            print(f'Foram necessários {cont1} palpites para adivinhar o número correto.')
            break
        if numjog > numpc: # Quase.
            print('Quase! O número correto é menor!')
        if numjog < numpc: # Quase lá.
            print('Quase! O número correto é maior!')
        cont1 += 1 #Contador de vezes.
else: # Caso contrário, programa en-cer-ra-do.
    print('SENHA ERRADA!!!!!!!!!!!!!!!!!!!!!!!!!!')