import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tools import Images, SpriteLists

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(1)
        self.screen = pg.display.set_mode((windowSizeX, windowSizeY))
        pg.display.set_icon(Images.icon)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_map()

    def load_map(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, './tools/map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    Wall(self, col, row)
                if tile == ',':
                    Space(self, col, row)
                if tile == 'f':
                    Floor(self, col, row)
        self.draw()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.onMode = True
        while self.onMode:
            self.dt = self.clock.tick(FPS)
            self.events()

    def quit(self):
        pg.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                """pos = pg.mouse.get_pos()
                empty_clicked_sprites = [
                    s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                for sprite in empty_clicked_sprites:
                    sprite.addStudent()"""
                print("ok")
                self.onMode = False


    def play1(self):
        self.run()
        print("jogador um jogou\n")

    def play2(self):
        self.run()
        print("jogador dois jogou\n")

# create the game object
g = Game()
g.new()
while True:
    g.play1()
    g.play2()