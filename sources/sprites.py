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
    def __init__(self, button, text):
        #self.groups = game.all_sprites
        #pg.sprite.Sprite.__init__(self, self.groups)
        #self.game = game
        self.image = pg.Surface([155, 40])
        self.image.fill((LIGHTGREY))
        (x,y,x1,y1) = button
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = (x + x1)/2
        self.rect.y = (y + y1)/2
        self.font = pg.font.SysFont(FONT, textSize, False, False)
        self.textRender = self.font.render(text, 1, (WHITE))
        self.image.blit(self.textRender, [textSize, textSize])