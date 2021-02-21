import pygame as pg
import sys
from os import path
import random as rand
from settings import *
from sprites import *
from tools import Images, SpriteLists, GenerateTable, Places, Goals
from classes import player

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(1)
        self.screen = pg.display.set_mode((windowSizeX, windowSizeY))
        pg.display.set_icon(Images.icon)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_maps()

    def load_maps(self):
        game_folder = path.dirname(__file__)
        self.mapFGA_data = []
        with open(path.join(game_folder, './../tools/map.txt'), 'rt') as f:
            for line in f:
                self.mapFGA_data.append(line)

        self.mapUAC1_data = []
        with open(path.join(game_folder, './../tools/mapUAC1.txt'), 'rt') as f:
            for line in f:
                self.mapUAC1_data.append(line)

        self.mapUAC2_data = []
        with open(path.join(game_folder, './../tools/mapUAC2.txt'), 'rt') as f:
            for line in f:
                self.mapUAC2_data.append(line)

        self.mapUED_data = []
        with open(path.join(game_folder, './../tools/mapUED.txt'), 'rt') as f:
            for line in f:
                self.mapUED_data.append(line)

        self.mapRU_data = []
        with open(path.join(game_folder, './../tools/mapRU.txt'), 'rt') as f:
            for line in f:
                self.mapRU_data.append(line)

    def new(self, number):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        if number == 0:
            map = self.mapFGA_data

        if number == 1:
            map = self.mapUAC1_data

        if number == 2:
            map = self.mapUAC2_data

        if number == 3:
            map = self.mapUED_data

        if number == 4:
            map = self.mapRU_data

        for row, tiles in enumerate(map):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    Wall(self, col, row)
                if tile == '1' or tile == '2' or tile  == '3' or tile == '4' or tile == '5' or tile == '6' or tile == '7' or tile == '8' or tile == '9' or tile == 'a' or tile == 'b' or tile == 'c':
                    Text(self, tile, col, row, number)
        self.screen = pg.display.set_mode((windowSizeX, windowSizeY))
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def run(self):
        self.new(4)
        self.onMode = True
        while self.onMode:
            self.dt = self.clock.tick(FPS)
            self.events()

    def quit(self):
        pg.quit()
        sys.exit()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                empty_clicked_sprites = [
                    s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                for sprite in empty_clicked_sprites:
                    sprite.addStudent()
                print("ok")
                self.onMode = False


    def play1(self, nome):
        self.run()
        print("jogador ", nome, " jogou\n")

    def play2(self, nome):
        self.run()
        print("jogador ", nome, " jogou\n")

    def play3(self, nome):
        self.run()
        print("jogador ", nome, " jogou\n")

    def play4(self, nome):
        self.run()
        print("jogador ", nome, " jogou\n")

    def play5(self, nome):
        self.run()
        print("jogador ", nome, " jogou\n")

    def play6(self, nome):
        self.run()
        print("jogador ", nome, " jogou\n")

    def choose(self, name):
        choose = Game()
        choose.scream = pg.display.set_mode((SCREAMSIZE))
        choose.clock = pg.time.Clock()
        onMode = True
        decision = 0
        while onMode:
            choose.font = pg.font.SysFont(FONT, textSize)
            choose.name = choose.font.render(name, True, WHITE)
            choose.scream.blit(choose.name, [25, 10])
            choose.choose = choose.font.render("Escolha seus estudantes", True, WHITE)
            choose.scream.blit(choose.choose, [25, 30])

            buttonEng = pg.Rect(40, 70, 100, 15)
            #pg.draw.rect(choose.screen, WHITE, buttonEng)
            choose.eng = choose.font.render("Engenharias", True, RED)
            choose.scream.blit(choose.eng,[50, 70])

            buttonSoftware = pg.Rect(40,100,100,15)
            #pg.draw.rect(choose.scream,WHITE,buttonSoftware)
            choose.software = choose.font.render("Software", True, RED)
            choose.scream.blit(choose.software,[50, 100])

            buttonEletronica = pg.Rect(40,130,100,15)
            #pg.draw.rect(choose.scream,WHITE,buttonEletronica)
            choose.eletronica = choose.font.render("Eletrônica", True, RED)
            choose.scream.blit(choose.eletronica,[50, 130])

            buttonAero = pg.Rect(40,160,100,15)
            #pg.draw.rect(choose.scream,WHITE,buttonAero)
            choose.aero = choose.font.render("Aeroespacial", True, RED)
            choose.scream.blit(choose.aero,[50, 160])

            buttonAuto = pg.Rect(40,190,100,15)
            #pg.draw.rect(choose.scream,WHITE,buttonAuto)
            choose.auto = choose.font.render("Automotiva", True, RED)
            choose.scream.blit(choose.auto,[50, 190])

            buttonEnergia = pg.Rect(40,220,100,15)
            #pg.draw.rect(choose.scream,WHITE,buttonEnergia)
            choose.energia = choose.font.render("Energia", True, RED)
            choose.scream.blit(choose.energia,[50, 220])

            #choose.scream.fill(LIGHTGREY)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    choose.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if buttonEng.collidepoint(event.pos):
                            decision = 1
                            onMode = False
                        if buttonSoftware.collidepoint(event.pos):
                            decision = 2
                            onMode = False
                        if buttonEletronica.collidepoint(event.pos):
                            decision = 3
                            onMode = False
                        if buttonAero.collidepoint(event.pos):
                            decision = 4
                            onMode = False
                        if buttonAuto.collidepoint(event.pos):
                            decision = 5
                            onMode = False
                        if buttonEnergia.collidepoint(event.pos):
                            decision = 6
                            onMode = False
            pg.display.update()
        return decision

    def random (self, list_goals):
        ok = True
        a = rand.randint(1,14)
        for goals in list_goals:
            if a == goals:
                ok = False

        if ok:
            return a
        else:
            return self.random (list_goals)

    def start_game(self, argv):
        list_goals = [0, 0, 0, 0, 0, 0]
        decision = [0,0,0,0,0,0,0]
        number = len(sys.argv)
        for i in range (1,number):
            decision[i] = self.choose(sys.argv[i])

        player1 = player.Player(sys.argv[1])
        player1.add_decision(decision[1])
        goals1 = rand.randint(1,14)
        #print("1: ",goals1)
        list_goals[0] = goals1
        player1.add_goals(goals1)

        player2 = player.Player(sys.argv[2])
        player2.add_decision(decision[2])
        goals2 = self.random(list_goals)
        #print("2: ", goals2)
        list_goals[1] = goals2
        player2.add_goals(goals2)

        player3 = player.Player(sys.argv[3])
        player3.add_decision(decision[4])
        goals3 = self.random(list_goals)
        #print("3: ", goals3)
        list_goals[2] = goals3
        player3.add_goals(goals3)

        if len(sys.argv) >= 5:
            player4 = player.Player(sys.argv[4])
            player4.add_decision(decision[4])
            goals4 = self.random(list_goals)
            #print("4: ", goals4)
            list_goals[3] = goals4
            player4.add_goals(goals4)

            if len (sys.argv) >= 6:
                player5 = player.Player(sys.argv[5])
                player5.add_decision(decision[5])
                goals5 = self.random(list_goals)
                #print("5: ", goals5)
                list_goals[4] = goals5
                player5.add_goals(goals5)

                if len(sys.argv) == 7:
                    player6 = player.Player(sys.argv[6])
                    player6.add_decision(decision[6])
                    goals6 = self.random(list_goals)
                    #print("6: ", goals6)
                    list_goals[5] = goals6
                    player6.add_goals(goals6)

    def arrange(self):
        pass