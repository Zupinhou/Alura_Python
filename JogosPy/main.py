import guessing
import hangman
import jankenpon
from pyfiglet import figlet_format


print(figlet_format('JOGOS', font='standard'))

print('[1] Sorteio\n[2] Forca\n[3] Jankenpon\n[0] Sair\n')
game = int(input('Qual jogo? '))

if (game == 1):
    guessing.play()
elif (game == 2):
    hangman.play()
elif (game == 3):
    jankenpon.play()
elif (game == 0):
    print("Saindo...")
