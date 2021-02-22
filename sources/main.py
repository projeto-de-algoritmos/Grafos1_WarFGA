import sys
from classes import Game

# create the game object
g = Game.Game()

# how many players have
if len(sys.argv) <= 3 or len(sys.argv) > 7:
    print ("Número inválido de jogadores.")
    g.quit()

g.count = 0
g.start_game(sys.argv)
g.map_mumber = 0
g.players = len(sys.argv) -1
while True:
	g.arrange(g.map_mumber)
		#"""g.play1()
	    #g.play2()
	    #g.play3()
	    #if g.players >= 4:
	     #   g.play4()
	      #  if g.players >= 5:
	       #     g.play5()
	        #    if g.players == 6:
	         #       g.play6()"""