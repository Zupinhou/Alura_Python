import adivinhacao
import forca
from pyfiglet import figlet_format


print(figlet_format('JOGOS', font='standard'))

print('[1] Sorteio\n[2] Forca\n[0] Sair\n')
jogo = int(input('Qual jogo? '))

if (jogo == 1):
    adivinhacao.jogar()
elif (jogo == 2):
    forca.jogar()
elif (jogo == 0):
    print("Saindo...")
