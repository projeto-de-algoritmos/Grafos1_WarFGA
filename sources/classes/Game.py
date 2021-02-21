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

        self.mapContainers_data = []
        with open(path.join(game_folder, './../tools/mapContainers.txt'), 'rt') as f:
            for line in f:
                self.mapContainers_data.append(line)

        self.mapPredioNovo_data = []
        with open(path.join(game_folder, './../tools/mapPredioNovo.txt'), 'rt') as f:
            for line in f:
                self.mapPredioNovo_data.append(line)

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

        if number == 5:
            map = self.mapContainers_data

        if number == 6:
            map = self.mapPredioNovo_data

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
        self.new(6)
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

    def choose(self, name, decision):
        choose = Game()

        # create a new screen to choose the "color"
        choose.scream = pg.display.set_mode((SCREAMSIZE))
        choose.clock = pg.time.Clock()
        onMode = True

        while onMode:
            choose.font = pg.font.SysFont(FONT, textSize, False, False)
            choose.name = choose.font.render(name, False, WHITE)
            choose.scream.blit(choose.name, [25, 10])
            choose.choose = choose.font.render("Escolha seus estudantes", False, WHITE)
            choose.scream.blit(choose.choose, [25, 30])

            # don't let them choose the same "color"
            if decision[0] == 0:
                buttonEng = pg.Rect(40, 70, 100, 15)
                #pg.draw.rect(choose.screen, WHITE, buttonEng)
                choose.eng = choose.font.render("Engenharias", False, RED)
                choose.scream.blit(choose.eng,[50, 70])

            if decision[1] == 0:
                buttonSoftware = pg.Rect(40,100,100,15)
                #pg.draw.rect(choose.scream,WHITE,buttonSoftware)
                choose.software = choose.font.render("Software", False, RED)
                choose.scream.blit(choose.software,[50, 100])

            if decision[2] == 0:
                buttonEletronica = pg.Rect(40,130,100,15)
                #pg.draw.rect(choose.scream,WHITE,buttonEletronica)
                choose.eletronica = choose.font.render("Eletrônica", False, RED)
                choose.scream.blit(choose.eletronica,[50, 130])

            if decision [3] == 0:
                buttonAero = pg.Rect(40,160,100,15)
                #pg.draw.rect(choose.scream,WHITE,buttonAero)
                choose.aero = choose.font.render("Aeroespacial", False, RED)
                choose.scream.blit(choose.aero,[50, 160])

            if decision[4] == 0:
                buttonAuto = pg.Rect(40,190,100,15)
                #pg.draw.rect(choose.scream,WHITE,buttonAuto)
                choose.auto = choose.font.render("Automotiva", False, RED)
                choose.scream.blit(choose.auto,[50, 190])

            if decision[5] == 0:
                buttonEnergia = pg.Rect(40,220,100,15)
                #pg.draw.rect(choose.scream,WHITE,buttonEnergia)
                choose.energia = choose.font.render("Energia", False, RED)
                choose.scream.blit(choose.energia,[50, 220])

            #choose.scream.fill(LIGHTGREY)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    choose.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if decision[0] == 0:
                            if buttonEng.collidepoint(event.pos):
                                decision[0] = 1
                                onMode = False
                        if decision[1] == 0:
                            if buttonSoftware.collidepoint(event.pos):
                                decision[1] = 2
                                onMode = False
                        if decision[2] == 0:
                            if buttonEletronica.collidepoint(event.pos):
                                decision[2] = 3
                                onMode = False
                        if decision[3] == 0:
                            if buttonAero.collidepoint(event.pos):
                                decision[3] = 4
                                onMode = False
                        if decision[4] == 0:
                            if buttonAuto.collidepoint(event.pos):
                                decision[4] = 5
                                onMode = False
                        if decision[5] == 0:
                            if buttonEnergia.collidepoint(event.pos):
                                decision[5] = 6
                                onMode = False
            pg.display.update()
        return decision

    def random (self, list_goals):
        # checks if that "goal" has already been given
        ok = True
        a = rand.randint(1,14)
        for goals in list_goals:
            if a == goals:
                ok = False

        if ok:
            return a
        else:
            return self.random (list_goals) #continue in the loop until it's a "new goal"

    def randomClasses(self, places):
        # checks if that "country" has already been given
        ok = True
        a = rand.randint(1,42)
        for p in places:
            if a == p:
                ok = False

        if ok:
            return a
        else:
            return self.randomClasses(places) #continue in the loop until it's a "new country"

    def distributeClasses(self, number):
        places = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # distribute "countries" to players
        if number == 4:
            j = 0
            k = 14
            l = 28

            for i in range (14):
                class1 = self.randomClasses(places)
                places[j] = class1
                self.player1.add_classes(class1)
                j = j + 1

                class2 = self.randomClasses(places)
                places[k] = class2
                self.player2.add_classes(class2)
                k = k + 1

                class3 = self.randomClasses(places)
                places[l] = class3
                self.player3.add_classes(class3)
                l = l + 1

        if number == 5:
            j = 0
            k = 10
            l = 20
            m = 30

            for i in range (10):
                class1 = self.randomClasses(places)
                places[j] = class1
                self.player1.add_classes(class1)
                j = j + 1

                class2 = self.randomClasses(places)
                places[k] = class2
                self.player2.add_classes(class2)
                k = k + 1

                class3 = self.randomClasses(places)
                places[l] = class3
                self.player3.add_classes(class3)
                l = l + 1

                class4 = self.randomClasses(places)
                places[m] = class4
                self.player4.add_classes(class4)
                m = m + 1

            class1 = self.randomClasses(places)
            places[j] = class1
            self.player1.add_classes(class1)
            j = j + 1

            class2 = self.randomClasses(places)
            places[k] = class2
            self.player2.add_classes(class2)
            k = k + 1

        if number == 6:
            j = 0
            k = 8
            l = 16
            m = 24
            n = 32

            for i in range (8):
                class1 = self.randomClasses(places)
                places[j] = class1
                self.player1.add_classes(class1)
                j = j + 1

                class2 = self.randomClasses(places)
                places[k] = class2
                self.player2.add_classes(class2)
                k = k + 1

                class3 = self.randomClasses(places)
                places[l] = class3
                self.player3.add_classes(class3)
                l = l + 1

                class4 = self.randomClasses(places)
                places[m] = class4
                self.player4.add_classes(class4)
                m = m + 1

                class5 = self.randomClasses(places)
                places[n] = class5
                self.player5.add_classes(class5)
                n = n + 1

            class1 = self.randomClasses(places)
            places[j] = class1
            self.player1.add_classes(class1)
            j = j + 1

            class2 = self.randomClasses(places)
            places[k] = class2
            self.player2.add_classes(class2)
            k = k + 1

        if number == 7:
            j = 0
            k = 7
            l = 14
            m = 21
            n = 28
            o = 35

            for i in range (7):
                class1 = self.randomClasses(places)
                places[j] = class1
                self.player1.add_classes(class1)
                j = j + 1

                class2 = self.randomClasses(places)
                places[k] = class2
                self.player2.add_classes(class2)
                k = k + 1

                class3 = self.randomClasses(places)
                places[l] = class3
                self.player3.add_classes(class3)
                l = l + 1

                class4 = self.randomClasses(places)
                places[m] = class4
                self.player4.add_classes(class4)
                m = m + 1

                class5 = self.randomClasses(places)
                places[n] = class5
                self.player5.add_classes(class5)
                n = n + 1

                class6 = self.randomClasses(places)
                places[o] = class6
                self.player6.add_classes(class6)
                o = o + 1

            #print (self.player1.places)
            #print (self.player2.places)
            #print (self.player3.places)
            #print (self.player4.places)
            #print (self.player5.places)
            #print (self.player6.places)

    def start_game(self, argv):
        # variables
        list_goals = [0, 0, 0, 0, 0, 0]
        decision = [0,0,0,0,0,0,0]
        number = len(sys.argv)

        # decide de "color" of the players
        for i in range (1,number):
            decision = self.choose(sys.argv[i], decision)

        # create the players
        goals1 = rand.randint(1,14)
        #print("1: ",goals1)
        list_goals[0] = goals1
        self.player1 = player.Player(sys.argv[1], decision[1], goals1)

        goals2 = rand.randint(1,14)
        #print("2: ",goals2)
        list_goals[1] = goals2
        self.player2 = player.Player(sys.argv[2], decision[2], goals2)

        goals3 = rand.randint(1,14)
        #print("3: ",goals3)
        list_goals[2] = goals3
        self.player3 = player.Player(sys.argv[3], decision[3], goals3)

        if len(sys.argv) >= 5:
            goals4 = rand.randint(1,14)
            #print("4: ",goals4)
            list_goals[3] = goals4
            self.player4 = player.Player(sys.argv[4], decision[4], goals4)

            if len (sys.argv) >= 6:
                goals5 = rand.randint(1,14)
                #print("5: ",goals5)
                list_goals[4] = goals5
                self.player5 = player.Player(sys.argv[5], decision[5], goals5)

                if len(sys.argv) == 7:
                    goals6 = rand.randint(1,14)
                    #print("6: ",goals6)
                    list_goals[5] = goals6
                    self.player6 = player.Player(sys.argv[6], decision[6], goals6)

        self.distributeClasses(number)

    def arrange(self):
        tam = len (self.player1.places)
        