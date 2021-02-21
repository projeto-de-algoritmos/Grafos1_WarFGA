import sys
from classes import Game

# create the game object
g = Game.Game()
if len(sys.argv) <= 3 or len(sys.argv) > 7:
    print ("Número inválido de jogadores.")
    g.quit()

g.start_game(len(sys.argv))
while True:
    g.arrange()
    if len(sys.argv) >= 4:
        g.play1(sys.argv[1])
        g.play2(sys.argv[2])
        g.play3(sys.argv[3])
        if len(sys.argv) >= 5:
            g.play4(sys.argv[4])
            if len(sys.argv) >= 6:
                g.play5(sys.argv[5])
                if len(sys.argv) == 7:
                    g.play6(sys.argv[6])
