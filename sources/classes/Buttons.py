import pygame as pg
import sys
from os import path
import random as rand
from settings import *
from sprites import *
from tools import Images, SpriteLists, GenerateTable, Places, Goals
from classes import player

class Buttons ():

    def __init__(self):
        self.Buttons = "a"

    # nodes like buttons
    def buttons (self, text):
        if text == "FGA_UAC1":
            return pg.Rect(530,30,445,80)

        elif text == "FGA_UAC2":
            return pg.Rect(530,120,445,70)

        elif text == "FGA_UED":
            return pg.Rect(10, 40, 250, 130)
            
        elif text == "FGA_RU":
            return pg.Rect(700,240,280,110)

        elif text == "FGA_CONTAINERS":
            return pg.Rect(20,190,230,110)

        elif text == "FGA_PREDIONOVO":
            return pg.Rect(10,360,190,110)

        elif text == "UAC1_BIBLIOTECA":
            return pg.Rect(810, 10, 270, 150)

        elif text == "UAC1_AUDITORIO":
            return pg.Rect(10,270,370,80)

        elif text == "UAC1_ESCADAS1":
            return pg.Rect(640,0,100,60)

        elif text == "UAC1_ESCADAS2":
            return pg.Rect(620,460,100,40)

        elif text == "UAC1_OBELISCO":
            return pg.Rect(10,10,190,40)

        elif text == "UAC1_SECRETARIA":
            return pg.Rect(360,10,130,40)

        elif text == "UAC1_WCF":
            return pg.Rect(360,430,60,30)

        elif text == "UAC1_WFM":
            return pg.Rect(430,430,60,30)

        elif text == "UAC1_SALASCOMPUT":
            return pg.Rect(10,390,250,70)

        elif text == "UAC1_SALASAULAS":
            return pg.Rect(810,170,270,290)

        elif text == "UAC1_ENTRADA":
            return pg.Rect(0,160,70,50)

        elif text == "UAC2_AUDITORIO":
            return pg.Rect(10,150,370,80)

        elif text == "UAC2_MESAS":
            return pg.Rect(10,110,370,30)

        elif text == "UAC2_BANHEIROS01":
            return pg.Rect(380,10,130,40)

        elif text == "UAC2_BANHEIROS10":
            return pg.Rect(360,370,130,30)

        elif text == "UAC2_PSICOLOGO":
            return pg.Rect(150,10,180,40)

        elif text == "UAC2_SALASAULAS":
            return pg.Rect(810,10,240,390)

        elif text == "UAC2_S10":
            return pg.Rect(10,330,250,70)

        elif text == "UAC2_ESCADAS1":
            return pg.Rect(640,0,100,50)

        elif text == "UAC2_ESCADAS2":
            return pg.Rect(620,350,100,60)

        elif text == ("UED_FISICA"):
            return pg.Rect(10,140,250,40)

        elif text == ("UED_QUIMICA"):
            return pg.Rect(810,140,250,40)

        elif text == ("UED_MOCAP"):
            return pg.Rect(830,10,230,80)

        elif text == ("UED_PED1"):
            return pg.Rect(10,10,230,40)

        elif text == ("UED_MESAS"):
            return pg.Rect(10,60,70,70)
    
        elif text == ("UED_PORTAO"):
            return pg.Rect(430,0,100,50)

        elif text == ("UED_CONTAINERS"):
            return pg.Rect(420,150,110,50)

        elif text == ("RU_MESAS"):
            return pg.Rect(290,110,600,40)

        elif text == ("RU_COZINHA"):
            return pg.Rect(270,30,570,50)

        elif text == ("RU_UNBAJA"):
            return pg.Rect(520,200,210,40)

        elif text == ("RU_DAENG"):
            return pg.Rect(30,200,250,40)

        elif text == ("RU_MULTIMIDIA"):
            return pg.Rect(290,200,220,40)
    
        elif text == ("RU_MAMUTES"):
            return pg.Rect(30,160,210,30)

        elif text == ("CONTAINERS_EJ"):
            return pg.Rect(20,10,280,100)

        elif text == ("CONTAINERS_1"):
            return pg.Rect(20,170,280,100)

        elif text == ("CONTAINERS_2"):
            return pg.Rect(590,170,290,100)

        elif text == ("CONTAINERS_3"):
            return pg.Rect(590,10,290,100)

        elif text == ("PREDIONOVO_ENTRADA"):
            return pg.Rect(310,0,270,290)

        elif text == ("PREDIONOVO_SALA2"):
            return pg.Rect(20,190,280,100)

        elif text == ("PREDIONOVO_SALA3"):
            return pg.Rect(590,10,290,280)

        elif text == ("PREDIONOVO_SALA4"):
            return pg.Rect(20,10,280,170)