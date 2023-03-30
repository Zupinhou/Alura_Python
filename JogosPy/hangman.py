import random
from pyfiglet import figlet_format


def play():

    print(figlet_format('FORCA', font='standard'))

    hangmanlst = []

    word = chosen_animal()
    for letters in word:
        hangmanlst.append('_')

    print(hangmanlst)

    hanged = False
    hit = False
    flaws = 0

    while (not hit and not hanged):

        kick = input('Chute uma letra: ').lower().strip()

        if kick not in hangmanlst:
            if kick in word:
                check_kick(word, kick, hangmanlst)
            else:
                flaws += 1

            hanged = flaws == 5
            print(hangmanlst)

            if ('_' not in hangmanlst):
                print('Parabéns, você ganhou!')
                break
            if (flaws == 5):
                print(
                    f'Tente novamente, você não acertou a palavra {word}!')

        else:
            print('Letra repetida! Use outra.')


def chosen_animal():
    with open('animals.txt', 'r') as file:
        animals = []
        for linha in file:
            linha = linha.strip()
            animals.append(linha)
    word = random.choice(animals).lower().strip()
    return word


def check_kick(word, kick, hangmanlst):
    i = 0
    for letter in word:
        if (letter == kick):
            hangmanlst[i] = letter
        i += 1


if (__name__ == "__main__"):
    play()
