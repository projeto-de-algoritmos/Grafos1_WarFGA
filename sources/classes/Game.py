import pygame as pg
import sys
from os import path
from time import sleep
import random as rand
from settings import *
from sprites import *
from tools import Images, SpriteLists, Places, Goals, GenerateFGA
from classes import player, Buttons, Node

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(1)
        self.screen = pg.display.set_mode((windowSizeX, windowSizeY))
        pg.display.set_icon(Images.icon)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.load_map()
    
    def load_map(self):
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

        self.mapCONTAINERS_data = []
        with open(path.join(game_folder, './../tools/mapContainers.txt'), 'rt') as f:
            for line in f:
                self.mapCONTAINERS_data.append(line)

        self.mapPredioNovo_data = []
        with open(path.join(game_folder, './../tools/mapPredioNovo.txt'), 'rt') as f:
            for line in f:
                self.mapPredioNovo_data.append(line)

    def load_data(self):
        self.graph = Places.places
        self.graphFGA = Places.placesFGA
        self.graphUAC1 = Places.placesUAC1
        self.graphUAC2 = Places.placesUAC2
        self.graphUED = Places.placesUED
        self.graphRU = Places.placesRU
        self.graphPredioNovo = Places.placesPredioNovo
        self.graphContainers = Places.placesContainers
        #self.edges = GenerateFGA.createALL()
        #self.currentGraph = self.graphFGA

    def newBackground (self):
        # initialize all variables and do all the setup for a new game
        self.screen = pg.display.set_mode((windowSizeX, windowSizeY))
        self.screen.fill(BGCOLOR)
        self.all_sprites = pg.sprite.Group()
        map = []

        if self.map_number == 0:
            map = self.mapFGA_data

        if self.map_number == 1:
            map = self.mapUAC1_data

        if self.map_number == 2:
            map = self.mapUAC2_data

        if self.map_number == 3:
            map = self.mapUED_data

        if self.map_number == 4:
            map = self.mapRU_data

        if self.map_number == 5:
            map = self.mapPredioNovo_data

        if self.map_number == 6:
            map = self.mapCONTAINERS_data

        for row, tiles in enumerate(map):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    Wall(self, col, row)
                if tile == '1' or tile == '2' or tile  == '3' or tile == '4' or tile == '5' or tile == '6' or tile == '7' or tile == '8' or tile == '9' or tile == 'a' or tile == 'b' or tile == 'c':
                    Text(self, tile, col, row, self.map_number)
        
        #self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        exit = self.font.render("Finish your turn" , True, RED)
        self.screen.blit(exit, EXIT)
        name = self.font.render(("Vez do jogador: " + self.currentPlayer.name) , True, RED)
        self.screen.blit(name, PLAYER)
        pg.display.update()
        pg.display.flip()

    def rollDices(self, attacker, enemy):
        dice1 = dice2 = dice3 = dice4 = dice5 = dice6 = 0

        a = attacker
        e = enemy
        
        you = self.currentPlayer.nodeStudents[a]
        them = self.currentPlayer.nodeStudents[e]

        if you >= 2:
            dice1 = rand.randint(1, 6)
            print("Dice1: ", dice1)
        if you >= 3:
            dice2 = rand.randint(1, 6)
            print("Dice2: ", dice2)
        if you >= 4:
            dice3 = rand.randint(1, 6)
            print("Dice3: ", dice3)

        if them >= 1:
            dice4 = rand.randint(1,6)
            print("Dice4: ", dice4)
        if them >= 2:
            dice5 = rand.randint(1,6)
            print("Dice5: ", dice5)
        if them >= 3:
            dice6 = rand.randint(1,6)
            print("Dice6: ", dice6)

        def greater (n1, n2, n3):
            if n1 >= n2 and n1 >= n2:
               return n1
            elif n2 >= n1 and n2 >= n3:
                return n2
            else:
                return n3

        greaterYou = greater(dice1, dice2, dice3)
        print("Seu maior dado: ", greaterYou)
        greaterThem = greater(dice4, dice5, dice6)
        print ("Maior dado do inimigo: ", greaterThem)

        if greaterThem >= greaterYou:
            self.player1.rmv_students(a)
            self.player2.rmv_students(a)
            self.player3.rmv_students(a)
            if self.players >= 4:
                self.player4.rmv_students(a)
            if self.players >= 5:
                self.player5.rmv_students(a)
            if self.players == 6:
                self.player6.rmv_students(a)
        else:
            self.player1.rmv_students(e)
            self.player2.rmv_students(e)
            self.player3.rmv_students(e)
            if self.players >= 4:
                self.player4.rmv_students(e)
            if self.players >= 5:
                self.player5.rmv_students(e)
            if self.players == 6:
                self.player6.rmv_students(e)

        qtd = self.player1.qtdStudents(e)
        if qtd <= 0:
            return 1

        else:
            return 0

    def attack (self, place):
        can = False
        n = []
        button1 = button2 = button3 = button4 = button5 = button6 = (0,0,0,0)
        n = [0, 0, 0, 0, 0, 0]
        count = 0
        self.screen.fill (BLACK)
        for i in self.graph[place][1]:
            for j in self.currentPlayer.places:
                if i == j:
                    if self.currentPlayer.nodeStudents[i] > 1:
                        can = True
                        n[count] = j
                        count = count + 1
                        print ("vc pode atacar de ", j)

        if can == False:
            print ("Você não pode atacar")
            return

        wait = True
        while wait:
            y = 180
            count = 1
            if can == True:
                for i in n:
                    if i != 0:
                        places = str(i)
                        text = self.font.render(("Pode atacar de " + places), False, WHITE)
                        self.screen.blit(text, [430, y])
                        if count == 1:
                            button1 = (430, y, 100, 20)
                        if count == 2:
                            button2 = (430, y, 100, 20)
                        if count == 3:
                            button3 = (430, y, 100, 20)
                        if count == 4:
                            button4 = (430, y, 100, 20)
                        if count == 5:
                            button5 = (430, y, 100, 20)
                        if count == 6:
                            button6 = (430, y, 100, 20)
                        y = y + 40
                        count = count + 1
            else:
                text = self.font.render("Não pode atacar", False, WHITE)
                self.screen.blit(text, [430, y])

            pg.display.update()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    if can == True:
                        b1 = pg.Rect(button1)
                        b2 = pg.Rect(button2)
                        b3 = pg.Rect(button3)
                        b4 = pg.Rect(button4)
                        b5 = pg.Rect(button5)
                        b6 = pg.Rect(button6)
                        if b1.collidepoint(event.pos):
                            you = n[0]
                        elif b2.collidepoint(event.pos):
                            you = n[1]
                        elif b3.collidepoint(event.pos):
                            you = n[2]
                        elif b4.collidepoint(event.pos):
                            you = n[3]
                        elif b5.collidepoint(event.pos):
                            you = n[4]
                        elif b6.collidepoint(event.pos):
                            you = n[5]
                        else:
                            return
                        
                        #win = self.rollDices(you, place)
                        win = 0
                        wait = False
                        if win == 1:
                            while wait:
                                self.screen.fill (BLACK)  
                                text = self.font.render("Você ganhou!", False, WHITE)
                                self.screen.blit(text, [430, 180])

                                for p in self.player1.places:
                                    if p == place:
                                        self.player1.rmv_classes(place)

                                for p in self.player2.places:
                                    if p == place:
                                        self.player2.rmv_classes(place)

                                for p in self.player3.places:
                                    if p == place:
                                        self.player3.rmv_classes(place)

                                if self.players >= 4:
                                    for p in self.player4.places:
                                        if p == place:
                                            self.player4.rmv_classes(place)
                                if self.players >= 5:
                                    for p in self.player5.places:
                                        if p == place:
                                            self.player5.rmv_classes(place)
                                if self.players == 6:
                                    for p in self.player6.places:
                                        if p == place:
                                            self.player6.rmv_classes(place)

                                if self.currentPlayer == self.player1:
                                    self.player1.add_classes(place)
                                elif self.currentPlayer == self.player2:
                                    self.player2.add_classes(place)
                                elif self.currentPlayer == self.player3:
                                    self.player3.add_classes(place)
                                elif self.currentPlayer == self.player4:
                                    self.player4.add_classes(place)
                                elif self.currentPlayer == self.player5:
                                    self.player5.add_classes(place)
                                elif self.currentPlayer == self.player6:
                                    self.player6.add_classes(place)
                        wait = False
                        return
                       
    def showInformations(self, place):

        can = False

        if self.currentGraph == self.graphUAC2:
            place = place + 12
        if self.currentGraph == self.graphUED:
            place = place + 21

        if self.currentGraph == self.graphRU:
            place = place + 28

        if self.currentGraph == self.graphPredioNovo:
            place = place + 34

        if self.currentGraph == self.graphContainers:
            place = place + 38

        for p in self.player1.places:
            if p == place:
                self.owner = self.player1

        for p in self.player2.places:
            if p == place:
                self.owner = self.player2

        for p in self.player3.places:
            if p == place:
                self.owner = self.player3

        if self.players == 4:
            for p in self.player4.places:
                if p == place:
                    self.owner = self.player4

        if self.players == 5:
            for p in self.player5.places:
                if p == place:
                    self.owner = self.player5

        if self.players == 6:
            for p in self.player6.places:
                if p == place:
                    self.owner = self.player6

        #print (place)
        #print (self.owner.name)
        students = self.owner.nodeStudents[place]
        students = str(students)

        wait = True
        while wait:
            rect = pg.Rect(400, 150, 200, 200)
            pg.draw.rect(self.screen, BLACK, rect)
            text = self.font.render(("Informações") , True, WHITE)
            self.screen.blit(text, [410, 160])

            if self.owner == self.currentPlayer:
                text = self.font.render(("Seu território") , True, WHITE)
                text2 = self.font.render("Não pode atacar", True, WHITE)
            else:
                text = self.font.render(("Território de " + self.owner.name) , True, WHITE)
                text2 = self.font.render("Deseja atacar?", True, WHITE)
                no = self.font.render("Não", True, WHITE)
                buttonNo = pg.Rect (410,250,25,20)
                pg.draw.rect(self.screen, RED, buttonNo)
                self.screen.blit(no, [410, 250])
                yes = self.font.render("Sim", True, WHITE)
                buttonYes = pg.Rect(450,250,25,20)
                pg.draw.rect(self.screen, RED, buttonYes)
                self.screen.blit(yes, [450, 250])
            
            text3 = self.font.render(("Alunos: " + students), True, WHITE)
            self.screen.blit(text, [410, 180])
            self.screen.blit(text2, [410, 200])
            self.screen.blit(text3, [410, 300])
            pg.display.update()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    wait = False
                    if self.owner != self.currentPlayer:
                        if buttonYes.collidepoint(event.pos):
                            #self.attack(place)
                            can = True
                            print ("ataca")
                        if buttonNo.collidepoint(event.pos):
                            print ("n ataca")
                            can = False
        if can == True:
            self.attack(place)
        return

    def events(self):
        buttonFinish = pg.Rect(800, 450, 100, 20)
        #pg.draw.rect(self.screen, RED, buttonFinish)
        stay = False
        wait = True
        pg.display.flip()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.MOUSEBUTTONUP:
                if buttonFinish.collidepoint(event.pos):
                    self.onMode = False
                else:
                    for places in self.currentGraph:
                        button = pg.Rect(self.currentGraph[places][2])
                        if button.collidepoint(event.pos):
                            stay = True
                            print (self.currentGraph[places][0])

                            if self.map_number == 0:
                                self.map_number = places
                                if places == 1:
                                    self.currentGraph = self.graphUAC1
                                elif places == 2:
                                    self.currentGraph = self.graphUAC2
                                elif places == 3:
                                    self.currentGraph = self.graphUED
                                elif places == 4:
                                    self.currentGraph = self.graphRU
                                elif places == 5:
                                    self.currentGraph = self.graphPredioNovo
                                else:
                                    self.currentGraph = self.graphContainers

                            elif self.map_number == 1:
                                if places == 'a':
                                    places = 10
                                if places == 'b':
                                    places = 11
                                if places == 'c':
                                    places = 12
                                if places == 3 or places == 4:
                                    while wait:
                                        text = self.font.render("Você quer ir para o segundo andar?" , False, RED)
                                        self.screen.blit(text, MOVE)
                                        no = self.font.render("Não" , False, WHITE)
                                        self.screen.blit(no, NO)
                                        yes = self.font.render("Sim" , False, WHITE)
                                        self.screen.blit(yes, YES)
                                        buttonYes = pg.Rect(500, 330, 50, 20)
                                        buttonNo = pg.Rect(600,330,50,20)
                                        #pg.draw.rect(self.screen, RED, buttonYes)
                                        #pg.draw.rect(self.screen, RED, buttonNo)
                                        pg.display.update()
                                        pg.display.flip()
                                        for e in pg.event.get():
                                            if e.type == pg.QUIT:
                                                self.quit()

                                            if e.type == pg.MOUSEBUTTONUP and buttonYes.collidepoint(e.pos):
                                                wait = False
                                                self.map_number = 2
                                                self.currentGraph = self.graphUAC2
                                            elif e.type == pg.MOUSEBUTTONUP and buttonNo.collidepoint(e.pos):
                                                n = places
                                                self.showInformations(n)
                                                wait = False
                                else:
                                    n = places
                                    self.showInformations(n)

                            elif self.map_number == 2:
                                if places == 9 or places == 8:
                                    while wait:
                                        text = self.font.render("Você quer ir para o primeiro andar?" , False, RED)
                                        self.screen.blit(text, MOVE)
                                        no = self.font.render("Não" , False, WHITE)
                                        self.screen.blit(no, NO)
                                        yes = self.font.render("Sim" , False, WHITE)
                                        self.screen.blit(yes, YES)
                                        buttonYes = pg.Rect(500, 330, 50, 20)
                                        buttonNo = pg.Rect(600,330,50,20)
                                        #pg.draw.rect(self.screen, RED, buttonYes)
                                        #pg.draw.rect(self.screen, RED, buttonNo)
                                        pg.display.update()
                                        pg.display.flip()
                                        for e in pg.event.get():
                                            if e.type == pg.QUIT:
                                                self.quit()

                                            if e.type == pg.MOUSEBUTTONUP and buttonYes.collidepoint(e.pos):
                                                wait = False
                                                self.map_number = 1
                                                self.currentGraph = self.graphUAC1
                                            elif e.type == pg.MOUSEBUTTONUP and buttonNo.collidepoint(e.pos):
                                                n = places
                                                self.showInformations(n)
                                                wait = False
                                else:
                                    n = places
                                    self.showInformations(n)

                            elif self.map_number == 3:
                                if places == 7:
                                    while wait:
                                        text = self.font.render("Você quer ir para os containers?" , False, RED)
                                        self.screen.blit(text, MOVE)
                                        no = self.font.render("Não" , False, WHITE)
                                        self.screen.blit(no, NO)
                                        yes = self.font.render("Sim" , False, WHITE)
                                        self.screen.blit(yes, YES)
                                        buttonYes = pg.Rect(500, 330, 50, 20)
                                        buttonNo = pg.Rect(600,330,50,20)
                                        #pg.draw.rect(self.screen, RED, buttonYes)
                                        #pg.draw.rect(self.screen, RED, buttonNo)
                                        pg.display.update()
                                        pg.display.flip()
                                        for e in pg.event.get():
                                            if e.type == pg.QUIT:
                                                self.quit()

                                            if e.type == pg.MOUSEBUTTONUP and buttonYes.collidepoint(e.pos):
                                                wait = False
                                                self.map_number = 6
                                                self.currentGraph = self.graphContainers
                                            elif e.type == pg.MOUSEBUTTONUP and buttonNo.collidepoint(e.pos):
                                                n = places
                                                self.showInformations(n)
                                                wait = False
                                else:
                                    n = places
                                    self.showInformations(n)
                            else:
                                n = places
                                self.showInformations(n)

                            return

                    if stay == False:
                        self.map_number = 0
                        self.currentGraph = self.graphFGA
    
    def run(self):
        self.onMode = True
        while self.onMode:
            self.dt = self.clock.tick(FPS)
            self.newBackground()
            self.events()

    def quit(self):
        pg.quit()
        sys.exit()

    def play1(self):
        self.map_number = 0
        self.currentGraph = self.graphFGA
        self.currentPlayer = self.player1
        self.run()
        print("jogador ", self.player1.name, " jogou\n")

    def play2(self):
        self.map_number = 0
        self.currentGraph = self.graphFGA
        self.currentPlayer = self.player2
        self.run()
        print("jogador ", self.player2.name, " jogou\n")

    def play3(self):
        self.map_number = 0
        self.currentGraph = self.graphFGA
        self.currentPlayer = self.player3
        self.run()
        print("jogador ", self.player3.name, " jogou\n")

    def play4(self):
        self.map_number = 0
        self.currentGraph = self.graphFGA
        self.currentPlayer = self.player4
        self.run()
        print("jogador ", self.player4.name, " jogou\n")

    def play5(self):
        self.map_number = 0
        self.currentGraph = self.graphFGA
        self.currentPlayer = self.player5
        self.run()
        print("jogador ", self.player5.name, " jogou\n")

    def play6(self):
        self.map_number = 0
        self.currentGraph = self.graphFGA
        self.currentPlayer = self.player6
        self.run()
        print("jogador ", self.player6.name, " jogou\n")

    def choose(self, name, decision):
        choose = Game()

        # create a new screen to choose the "color"
        choose.scream = pg.display.set_mode((SCREAMSIZE))
        choose.clock = pg.time.Clock()
        #choose.scream.fill(LIGHTGREY)
        onMode = True

        while onMode:
            choose.font = pg.font.SysFont(FONT, textSize, False, False)
            choose.name = choose.font.render(name, False, LIGHTGREY)
            choose.scream.blit(choose.name, [25, 10])
            choose.choose = choose.font.render("Escolha seus estudantes", False, LIGHTGREY)
            choose.scream.blit(choose.choose, [25, 30])

            # don't let them choose the same "color"
            if decision[0] == 0:
                buttonEng = pg.Rect(40, 70, 100, 15)
                #pg.draw.rect(choose.screen, LIGHTGREY, buttonEng)
                choose.eng = choose.font.render("Engenharias", False, RED)
                choose.scream.blit(choose.eng,[50, 70])

            if decision[1] == 0:
                buttonSoftware = pg.Rect(40,100,100,15)
                #pg.draw.rect(choose.scream,LIGHTGREY,buttonSoftware)
                choose.software = choose.font.render("Software", False, RED)
                choose.scream.blit(choose.software,[50, 100])

            if decision[2] == 0:
                buttonEletronica = pg.Rect(40,130,100,15)
                #pg.draw.rect(choose.scream,LIGHTGREY,buttonEletronica)
                choose.eletronica = choose.font.render("Eletrônica", False, RED)
                choose.scream.blit(choose.eletronica,[50, 130])

            if decision [3] == 0:
                buttonAero = pg.Rect(40,160,100,15)
                #pg.draw.rect(choose.scream,LIGHTGREY,buttonAero)
                choose.aero = choose.font.render("Aeroespacial", False, RED)
                choose.scream.blit(choose.aero,[50, 160])

            if decision[4] == 0:
                buttonAuto = pg.Rect(40,190,100,15)
                #pg.draw.rect(choose.scream,LIGHTGREY,buttonAuto)
                choose.auto = choose.font.render("Automotiva", False, RED)
                choose.scream.blit(choose.auto,[50, 190])

            if decision[5] == 0:
                buttonEnergia = pg.Rect(40,220,100,15)
                #pg.draw.rect(choose.scream,LIGHTGREY,buttonEnergia)
                choose.energia = choose.font.render("Energia", False, RED)
                choose.scream.blit(choose.energia,[50, 220])

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

    def printPlayer(self, player):
        if player == 1:
            p = self.player1
        elif player == 2:
            p = self.player2
        elif player == 3:
            p = self.player3
        elif player == 4:
            p = self.player4
        elif player == 5:
            p = self.player5
        else:
            p = self.player6

        self.screen = pg.display.set_mode((windowSizeX, windowSizeY))
        self.font = pg.font.SysFont(FONT, textSize, False, False)
        status = 0
        self.screen.fill(LIGHTGREY)
        x1 = 25
        x2 = 400
        y1 = 50
        y2 = 50
        self.name = self.font.render(("Seu lugares: " + p.name + " Você tem " + str(p.newStudents) + " para colocar") , True, DARKGREY)
        self.screen.blit(self.name, [x1, 10])
        for j in p.places:
            text = self.graph[j][0]
            self.name = self.font.render(text, False, DARKGREY)
            if status == 0:
                self.screen.blit(self.name, [x1, y1])
                y1 = y1 + 30
                pg.display.flip()
                pg.display.update()
                status = 1
            elif status == 1:
                self.screen.blit(self.name, [x2, y2])
                y2 = y2 + 30
                pg.display.flip()
                pg.display.update()
                status = 0

    def arrangePlayer(self, player):

        if player == 1:
            p = self.player1
        elif player == 2:
            p = self.player2
        elif player == 3:
            p = self.player3
        elif player == 4:
            p = self.player4
        elif player == 5:
            p = self.player5
        else:
            p = self.player6

        tam = len(p.places)
        p.newStudents = tam/2
        status = 0
        buttons = []
        pos = []
        x1 = 25
        x2 = 400
        y1 = 50
        y2 = 50
        onMode = True

        self.printPlayer(player)
        for j in p.places:
            if status == 0:
                buttons.append((x1, y1, 120, 10))
                pos.append(j)
                y1 = y1 + 30
                status = 1
            elif status == 1:
                buttons.append((x2, y2, 120, 10))
                pos.append(j)
                y2 = y2 + 30
                status = 0

        while onMode:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    for i in range(tam):
                        b = buttons[i]
                        position = pos[i]
                        button = pg.Rect(b)
                        if button.collidepoint(event.pos):
                            #teste = p.places[i]
                            #text = self.graph[teste][0]
                            p.newStudents = p.newStudents - 1
                            self.player1.add_students(position)
                            self.player2.add_students(position)
                            self.player3.add_students(position)
                            if self.players == 4:
                                self.player4.add_students(position)
                            if self.players == 5:
                                self.player5.add_students(position)
                            if self.players == 6:
                                self.player6.add_students(position)

                            pg.display.flip()
                            pg.display.update()
                            self.printPlayer(player)
                            if p.newStudents == 0:
                                onMode = False

    def arrange(self):
        self.map_number = 0
        self.arrangePlayer(1)
        self.arrangePlayer(2)
        self.arrangePlayer(3)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
        