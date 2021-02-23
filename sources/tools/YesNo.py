import pygame as pg
import sys
from settings import *

def YesNo():
	while True:
		screen = pg.display.set_mode((windowSizeX, windowSizeY))
		screen = pg.Surface([160, 40])
		font = pg.font.SysFont(FONT, textSize, False, False)
		no = font.render("Não" , False, WHITE)
	    screen.blit(no, [600, 330])
	    yes = font.render("Sim" , False, WHITE)
	    screen.blit(yes, [500, 330])
	    buttonYes = pg.Rect(500, 330, 50, 20)
	    buttonNo = pg.Rect(600,330,50,20)
	    #pg.draw.rect(screen, RED, buttonYes)
	    #pg.draw.rect(screen, RED, buttonNo)
	    pg.display.update()
	    pg.display.flip()
	    for event in pg.event.get():
	        if event.type == pg.QUIT:
	            pg.quit()
	            sys.quit()

	        if event.type == pg.MOUSEBUTTONUP and buttonYes.collidepoint(event.pos):
	            return 1
	        if event.type == pg.MOUSEBUTTONUP and buttonNo.collidepoint(e.pos):
	            return 0