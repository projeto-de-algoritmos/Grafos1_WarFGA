import pygame
from tools import Images


class Node(pygame.sprite.Sprite):
    def __init__(self, text, textSize):
        super().__init__()
        self.text = text
        self.students = 0
        self.students.type = " "


    def addStudents(self, qtd):
        self.students = self.students + qtd

    def rmvStudents(self, qtd):
        self.students = self.students - qtd

    def typeStudents(self, text):
        self.students.type = text

    def printStudents(self):
        print("total students: " , self.students)