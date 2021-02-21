import pygame as pg
import sys
from os import path
import random as rand
from settings import *
from sprites import *
from tools import Images, SpriteLists, GenerateTable, Places, Goals
from classes import player, Buttons

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

    def newBackground (self):
        # initialize all variables and do all the setup for a new game
        self.screen = pg.display.set_mode((windowSizeX, windowSizeY))
        self.screen.fill(BGCOLOR)
        self.all_sprites = pg.sprite.Group()

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
            map = self.mapContainers_data

        if self.map_number == 6:
            map = self.mapPredioNovo_data

        for row, tiles in enumerate(map):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    Wall(self, col, row)
                if tile == '1' or tile == '2' or tile  == '3' or tile == '4' or tile == '5' or tile == '6' or tile == '7' or tile == '8' or tile == '9' or tile == 'a' or tile == 'b' or tile == 'c':
                    Text(self, tile, col, row, self.map_number)

        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        b = Buttons.Buttons()
        # catch all events here
        if self.map_number == 0:
            buttonUAC1 = b.buttons("FGA_UAC1")
            #pg.draw.rect(self.screen, WHITE, buttonUAC1)

            buttonUAC2 = b.buttons("FGA_UAC2")
            #pg.draw.rect(self.screen, WHITE, buttonUAC2)

            buttonUED = b.buttons("FGA_UED")
            #pg.draw.rect(self.screen, WHITE, buttonUED)

            buttonRU = b.buttons("FGA_RU")
            #pg.draw.rect(self.screen, WHITE, buttonRU)

            buttonCONTAINERS = b.buttons("FGA_CONTAINERS")
            #pg.draw.rect(self.screen, WHITE, buttonCONTAINERS)

            buttonPREDIONOVO = b.buttons("FGA_PREDIONOVO")
            #pg.draw.rect(self.screen, WHITE, buttonPREDIONOVO)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    #pos = pg.mouse.get_pos()
                    #empty_clicked_sprites = [
                    #   s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                    #for sprite in empty_clicked_sprites:
                    #    sprite.addStudent()
                    #print("ok")
                    #self.onMode = Fals
                    if buttonUAC1.collidepoint(event.pos):
                        print ("UAC1")

                    elif buttonUAC2.collidepoint(event.pos):
                        print ("UAC2")

                    elif buttonUED.collidepoint(event.pos):
                        print ("UED")

                    elif buttonRU.collidepoint(event.pos):
                        print("RU")

                    elif buttonCONTAINERS.collidepoint(event.pos):
                        print("CONTAINERS")

                    elif buttonPREDIONOVO.collidepoint(event.pos):
                        print("PRÉDIO NOVO")

        elif self.map_number == 1:
            buttonBIBLIOTECA = b.buttons("UAC1_BIBLIOTECA")
            #pg.draw.rect(self.screen, WHITE, buttonBIBLIOTECA)

            buttonAUDITORIO = b.buttons("UAC1_AUDITORIO")
            #pg.draw.rect(self.screen, WHITE, buttonAUDITORIO)

            buttonESCADAS1 = b.buttons("UAC1_ESCADAS1")
            #pg.draw.rect(self.screen, WHITE, buttonESCADAS1)

            buttonESCADAS2 = b.buttons("UAC1_ESCADAS2")
            #pg.draw.rect(self.screen, WHITE, buttonESCADAS2)

            buttonMESAS = b.buttons("UAC1_MESAS")
            #pg.draw.rect(self.screen, WHITE, buttonMESAS)

            buttonOBELISCO = b.buttons("UAC1_OBELISCO")
            #pg.draw.rect(self.screen, WHITE, buttonOBELISCO)

            buttonSECRETARIA = b.buttons("UAC1_SECRETARIA")
            #pg.draw.rect(self.screen, WHITE, buttonSECRETARIA)

            buttonWCF = b.buttons("UAC1_WCF")
            #pg.draw.rect(self.screen, WHITE, buttonWCF)

            buttonWCM = b.buttons("UAC1_WFM")
            #pg.draw.rect(self.screen, WHITE, buttonWCM)

            buttonSALASCOMPUT = b.buttons("UAC1_SALASCOMPUT")
            #pg.draw.rect(self.screen, WHITE, buttonSALASCOMPUT)

            buttonSALASAULAS = b.buttons("UAC1_SALASAULAS")
            #pg.draw.rect(self.screen, WHITE, buttonSALASAULAS)

            buttonMESAS = b.buttons("UAC1_MESAS")
            #pg.draw.rect(self.screen, WHITE, buttonMESAS)

            buttonENTRADA = b.buttons("UAC1_ENTRADA")
            #pg.draw.rect(self.screen, WHITE, buttonENTRADA)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    #pos = pg.mouse.get_pos()
                    #empty_clicked_sprites = [
                    #   s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                    #for sprite in empty_clicked_sprites:
                    #    sprite.addStudent()
                    #print("ok")
                    #self.onMode = Fals
                    if buttonBIBLIOTECA.collidepoint(event.pos):
                        print ("BIBLIOTECA")

                    elif buttonAUDITORIO.collidepoint(event.pos):
                        print ("AUDITÓRIO")

                    elif buttonESCADAS1.collidepoint(event.pos):
                        print ("ESCADAS 1.1")

                    elif buttonESCADAS2.collidepoint(event.pos):
                        print ("ESCADAS 2.1")

                    elif buttonMESAS.collidepoint(event.pos):
                        print ("MESINHAS")

                    elif buttonOBELISCO.collidepoint(event.pos):
                        print ("O BELISCO")

                    elif buttonSECRETARIA.collidepoint(event.pos):
                        print ("SECRETARIA")

                    elif buttonWCF.collidepoint(event.pos):
                        print ("BANHEIRO FEMININO")

                    elif buttonWCM.collidepoint(event.pos):
                        print ("BANHEIRO MASCULINO")

                    elif buttonSALASCOMPUT.collidepoint(event.pos):
                        print ("SALAS COMPUTADORES")

                    elif buttonSALASAULAS.collidepoint(event.pos):
                        print ("SALAS DE AULAS")

                    elif buttonENTRADA.collidepoint(event.pos):
                        print ("ENTRADA")

        elif self.map_number == 2:
            buttonAUDITORIO = b.buttons("UAC2_AUDITORIO")
            #pg.draw.rect(self.screen, WHITE, buttonAUDITORIO)

            buttonMESAS = b.buttons("UAC2_MESAS")
            #pg.draw.rect(self.screen, WHITE, buttonMESAS)

            buttonBANHEIROS01 = b.buttons("UAC2_BANHEIROS01")
            #pg.draw.rect(self.screen, WHITE, buttonBANHEIROS01)

            buttonBANHEIROS10 = b.buttons("UAC2_BANHEIROS10")
            #pg.draw.rect(self.screen, WHITE, buttonBANHEIROS10)

            buttonPSICOLOGO = b.buttons("UAC2_PSICOLOGO")
            #pg.draw.rect(self.screen, WHITE, buttonPSICOLOGO)

            buttonSALASAULAS = b.buttons("UAC2_SALASAULAS")
            #pg.draw.rect(self.screen, WHITE, buttonSALASAULAS)

            buttonS10 = b.buttons("UAC2_S10")
            #pg.draw.rect(self.screen, WHITE, buttonS10)

            buttonESCADAS1 = b.buttons("UAC2_ESCADAS1")
            #pg.draw.rect(self.screen, WHITE, buttonESCADAS1)

            buttonESCADAS2 = b.buttons("UAC2_ESCADAS2")
            #pg.draw.rect(self.screen, WHITE, buttonESCADAS2)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    #pos = pg.mouse.get_pos()
                    #empty_clicked_sprites = [
                    #   s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                    #for sprite in empty_clicked_sprites:
                    #    sprite.addStudent()
                    #print("ok")
                    #self.onMode = Fals
                    if buttonAUDITORIO.collidepoint(event.pos):
                        print ("AUDITÓRIO PARTE DE CIMA")

                    elif buttonMESAS.collidepoint(event.pos):
                        print ("MESAS PERTO DO AUDITORIO")

                    elif buttonBANHEIROS01.collidepoint(event.pos):
                        print ("BANHEIRO PERTO DA S01")

                    elif buttonBANHEIROS10.collidepoint(event.pos):
                        print ("BANHEIRO PERTO DA S10")

                    elif buttonPSICOLOGO.collidepoint(event.pos):
                        print ("SALA DE ATENDIMENTO EMOCIONAL")

                    elif buttonSALASAULAS.collidepoint(event.pos):
                        print ("SALAS DE AULAS")

                    elif buttonS10.collidepoint(event.pos):
                        print ("SALA COM COMPUTADORES")

                    elif buttonESCADAS1.collidepoint(event.pos):
                        print ("Escadas perto da S01")

                    elif buttonESCADAS2.collidepoint(event.pos):
                        print ("Escadas perto da S10")

        elif self.map_number == 3:
            buttonFISICA = b.buttons("UED_FISICA")
            #pg.draw.rect(self.screen, WHITE, buttonFISICA)

            buttonQUIMICA = b.buttons("UED_QUIMICA")
            #pg.draw.rect(self.screen, WHITE, buttonQUIMICA)

            buttonMOCAP = b.buttons("UED_MOCAP")
            #pg.draw.rect(self.screen, WHITE, buttonMOCAP)

            buttonPED1 = b.buttons("UED_PED1")
            #pg.draw.rect(self.screen, WHITE, buttonPED1)

            buttonMESAS = b.buttons("UED_MESAS")
            #pg.draw.rect(self.screen, WHITE, buttonMESAS)

            buttonPORTAO = b.buttons("UED_PORTAO")
            #pg.draw.rect(self.screen, WHITE, buttonPORTAO)

            buttonCONTAINERS = b.buttons("UED_CONTAINERS")
            #pg.draw.rect(self.screen, WHITE, buttonCONTAINERS)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    #pos = pg.mouse.get_pos()
                    #empty_clicked_sprites = [
                    #   s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                    #for sprite in empty_clicked_sprites:
                    #    sprite.addStudent()
                    #print("ok")
                    #self.onMode = Fals
                    if buttonFISICA.collidepoint(event.pos):
                        print ("LAB FIS EXP")

                    elif buttonQUIMICA.collidepoint(event.pos):
                        print ("LAB QUIM EXP")

                    elif buttonMOCAP.collidepoint(event.pos):
                        print ("MOCAP")

                    elif buttonPED1.collidepoint(event.pos):
                        print ("LAB DE PED1")

                    elif buttonMESAS.collidepoint(event.pos):
                        print ("MESINHAS AMARELAS")

                    elif buttonPORTAO.collidepoint(event.pos):
                        print ("ENTRADA PORTÃO")

                    elif buttonCONTAINERS.collidepoint(event.pos):
                        print ("ENTRADA CONTAINERS")

        elif self.map_number == 4:
            buttonMESAS = b.buttons("RU_MESAS")
            #pg.draw.rect(self.screen, WHITE, buttonMESAS)

            buttonCOZINHA = b.buttons("RU_COZINHA")
            #pg.draw.rect(self.screen, WHITE, buttonCOZINHA)

            buttonUNBAJA = b.buttons("RU_UNBAJA")
            #pg.draw.rect(self.screen, WHITE, buttonUNBAJA)

            buttonDAENG = b.buttons("RU_DAENG")
            #pg.draw.rect(self.screen, WHITE, buttonDAENG)

            buttonMULTI = b.buttons("RU_MULTIMIDIA")
            #pg.draw.rect(self.screen, WHITE, buttonMULTI)

            buttonMAMUTES = b.buttons("RU_MAMUTES")
            #pg.draw.rect(self.screen, WHITE, buttonMAMUTES)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    #pos = pg.mouse.get_pos()
                    #empty_clicked_sprites = [
                    #   s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                    #for sprite in empty_clicked_sprites:
                    #    sprite.addStudent()
                    #print("ok")
                    #self.onMode = Fals
                    if buttonMESAS.collidepoint(event.pos):
                        print ("MESAS")

                    elif buttonCOZINHA.collidepoint(event.pos):
                        print ("LUGAR DE SE SERVIR")

                    elif buttonUNBAJA.collidepoint(event.pos):
                        print ("UNBaja")

                    elif buttonDAENG.collidepoint(event.pos):
                        print ("DAEng")

                    elif buttonMULTI.collidepoint(event.pos):
                        print ("Sala Multimida")

                    elif buttonMAMUTES.collidepoint(event.pos):
                        print ("Mamutes do Cerrado")

        elif self.map_number == 5:
            buttonEJ = b.buttons("CONTAINERS_EJ")
            #pg.draw.rect(self.screen, WHITE, buttonEJ)

            button1 = b.buttons("CONTAINERS_1")
            #pg.draw.rect(self.screen, WHITE, button1)

            button2 = b.buttons("CONTAINERS_2")
            #pg.draw.rect(self.screen, WHITE, button2)

            button3 = b.buttons("CONTAINERS_3")
            #pg.draw.rect(self.screen, WHITE, button3)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    #pos = pg.mouse.get_pos()
                    #empty_clicked_sprites = [
                    #   s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                    #for sprite in empty_clicked_sprites:
                    #    sprite.addStudent()
                    #print("ok")
                    #self.onMode = Fals
                    if buttonEJ.collidepoint(event.pos):
                        print ("EJ")

                    elif button1.collidepoint(event.pos):
                        print ("CONTAINER 1")

                    elif button2.collidepoint(event.pos):
                        print ("CONTAINER 2")

                    elif button3.collidepoint(event.pos):
                        print ("CONTAINER 3")

        elif self.map_number == 6:
            buttonENTRADA = b.buttons("PREDIONOVO_ENTRADA")
            #pg.draw.rect(self.screen, WHITE, buttonENTRADA)

            buttonSALA2 = b.buttons("PREDIONOVO_SALA2")
            #pg.draw.rect(self.screen, WHITE, buttonSALA2)

            buttonSALA3 = b.buttons("PREDIONOVO_SALA3")
            #pg.draw.rect(self.screen, WHITE, buttonSALA3)

            buttonSALA4 = b.buttons("PREDIONOVO_SALA4")
            #pg.draw.rect(self.screen, WHITE, buttonSALA4)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.MOUSEBUTTONUP:
                    #pos = pg.mouse.get_pos()
                    #empty_clicked_sprites = [
                    #   s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
                    #for sprite in empty_clicked_sprites:
                    #    sprite.addStudent()
                    #print("ok")
                    #self.onMode = Fals
                    if buttonENTRADA.collidepoint(event.pos):
                        print ("ENTRADA")

                    elif buttonSALA2.collidepoint(event.pos):
                        print ("SALA 2")

                    elif buttonSALA3.collidepoint(event.pos):
                        print ("SALA 3")

                    elif buttonSALA4.collidepoint(event.pos):
                        print ("SALA 4")



        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
    
    def run(self):
        self.newBackground()
        self.onMode = True
        while self.onMode:
            self.dt = self.clock.tick(FPS)
            self.events()

    def quit(self):
        pg.quit()
        sys.exit()

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
        while True:
            self.map_number = 6
            self.run()
            #print ("okay")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
        