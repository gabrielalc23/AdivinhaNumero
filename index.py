import random

def new_game():
    global sorteio, tentativas, pontos
    tentativas = 5
    pontos = 0
    sorteio = random.randint(1, 10)

tentativas = 5
pontos = 0
sorteio = random.randint(1, 10)

def testa_programa():
    global pontos
    tentativa = 0
    while tentativa < tentativas:
        igual = input('Digite o seu palpite: ')
        if igual.isdigit():
            igual = int(igual)
            if 0 <= igual <= 10:
                if igual == sorteio:
                    pontos = 100 - (tentativas - 1 - tentativa) * 10
                    print(f'Você acertou! Sua pontuação é de {pontos} pontos.')
                    break
                else:
                    print(f'Errou! O número era {sorteio}. Você tem {tentativas - tentativa - 1} tentativas restantes.')
            else:
                print('Digite um número entre 0 e 10.')
        else:
            print('Digite um número válido.')
        tentativa += 1

    print(f'Sua pontuação final é de {pontos} pontos.')
    play_again = input('Quer jogar novamente? (s/n) ')
    if play_again.lower() == 's':
        new_game()
        testa_programa()
    else:
        print('Até a próxima!')

new_game()
testa_programa()
