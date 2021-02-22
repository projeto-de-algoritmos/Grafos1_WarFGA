import pygame
from tools import Images


class Node(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.students = 1
        #self.students.type = ""

    def addStudents(self):
        self.students = self.students + 1

    def rmvStudents(self, qtd):
        self.students = self.students - qtd

   # def typeStudents(self, text):
    #    self.students.type = text

    def printStudents(self):
        print("total students: " , self.students)