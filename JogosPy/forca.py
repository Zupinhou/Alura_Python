import random
from pyfiglet import figlet_format


def jogar():

    print(figlet_format('FORCA', font='standard'))

    forcals = []

    palavra = animal_escolhido()
    for letras in palavra:
        forcals.append('_')

    print(forcals)

    enforcou = False
    acertou = False
    falhas = 0

    while (not acertou and not enforcou):

        chute = input('Chute uma letra: ').lower().strip()

        if chute not in forcals:
            if chute in palavra:
                verificar_chute(palavra, chute, forcals)
            else:
                falhas += 1

            enforcou = falhas == 5
            print(forcals)

            if ('_' not in forcals):
                print('Parabéns, você ganhou!')
                break
            if (falhas == 5):
                print(
                    f'Tente novamente, você não acertou a palavra {palavra}!')

        else:
            print('Letra repetida! Use outra.')


def animal_escolhido():
    with open('animais.txt', 'r') as arquivo:
        animais = []
        for linha in arquivo:
            linha = linha.strip()
            animais.append(linha)
    palavra = random.choice(animais).lower().strip()
    return palavra


def verificar_chute(palavra, chute, forcals):
    i = 0
    for letra in palavra:
        if (letra == chute):
            forcals[i] = letra
        i += 1


if (__name__ == "__main__"):
    jogar()
