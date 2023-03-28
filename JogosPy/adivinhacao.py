import random
from pyfiglet import figlet_format


def jogar():

    print(figlet_format('SORTEIO', font='standard'))

    sorteio = random.randrange(0, 101)

    print('Escolha a dificuldade.')
    print('[1] Fácil\n[2] Médio\n[3] Difícil')
    dificuldade = int(input('Digite o número da dificuldade: '))

    if (dificuldade == 1):
        rodada = rodada_total = 15
        pontos = 225
    elif (dificuldade == 2):
        rodada = rodada_total = 10
        pontos = 150
    elif (dificuldade == 3):
        rodada = rodada_total = 5
        pontos = 75

    while (rodada > 0):
        print(f'Está na rodada {rodada} de {rodada_total}')
        numero = int(input('Escreva um número entre 1 e 100: '))
        if numero < sorteio:
            print('O número é maior.')
            pontos -= 15
        elif numero > sorteio:
            print('Você errou. O número é menor...')
            pontos -= 15
        elif numero == sorteio:
            print('Você acertou. Parabéns!')
            print(f'Acertou e sua pontuação é {pontos}')
            break
        rodada -= 1


if (__name__ == '__main__'):
    jogar()
