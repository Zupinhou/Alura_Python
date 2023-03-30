import random
from pyfiglet import figlet_format


def play():

    print(figlet_format('sortition', font='standard'))

    sortition = random.randrange(0, 101)

    print('Escolha a dificuldade.')
    print('[1] Fácil\n[2] Médio\n[3] Difícil')
    difficulty = int(input('Digite o número da dificuldade: '))

    if (difficulty == 1):
        round = round_total = 15
        points = 225
    elif (difficulty == 2):
        round = round_total = 10
        points = 150
    elif (difficulty == 3):
        round = round_total = 5
        points = 75

    while (round > 0):
        print(f'Está na rodada {round} de {round_total}')
        number = int(input('Escreva um número entre 1 e 100: '))
        if number < sortition:
            print('O número é maior.')
            points -= 15
        elif number > sortition:
            print('Você errou. O número é menor...')
            points -= 15
        elif number == sortition:
            print('Você acertou. Parabéns!')
            print(f'Acertou e sua pontuação é {points}')
            break
        round -= 1


if (__name__ == '__main__'):
    play()
