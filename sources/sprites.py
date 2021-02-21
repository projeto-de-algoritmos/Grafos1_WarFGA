import pygame as pg
from settings import *
from tools import Places, SpriteLists

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * (TILESIZE)
        self.rect.y = y * (TILESIZE)

class Text(pg.sprite.Sprite):
    def __init__(self, game, char_int, x, y, number):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        if  char_int != 'a' and char_int != 'b' and char_int != 'c':
             char_int = int(char_int)

        if  number == 0:
            map = Places.placesFGA

        if  number == 1:
            map = Places.placesUAC1

        if  number == 2:
            map = Places.placesUAC2

        if  number == 3:
            map = Places.placesUED

        if  number == 4:
            map = Places.placesRU

        for node in map:
            if node ==  char_int:
                text = map[node][0]
                self.image = pg.Surface([155, 40])
                if number == 0:
                    self.image.fill((LIGHTGREY))
                else:
                    self.image.fill((DARKGREY))
                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.x = x * (TILESIZE)
                self.rect.y = y * (TILESIZE)
                self.font = pg.font.SysFont("Arial", textSize)
                self.textRender = self.font.render(text, 1, (WHITE))
                self.image.blit(self.textRender, [textSize, textSize])