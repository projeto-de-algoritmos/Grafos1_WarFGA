import pygame
from tools import SpriteLists, Images


class Node(pygame.sprite.Sprite):
    def __init__(self, width, height, text, textSize):
        super().__init__()
        self.text = text
        self.image = pygame.Surface([width, height])
        self.image.fill((207, 136, 169))
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("Arial", textSize)
        self.textRender = self.font.render(text, 1, (255, 255, 255))
        W = self.textRender.get_width()
        H = self.textRender.get_height()
        self.image.blit(self.textRender, [width/2 - W/2, height/2 - H/2])
        SpriteLists.empty_list.add(self)
        SpriteLists.all_sprites_list.add(self)
        self.students = 0

    def addStudent(self):
        self.students = self.students + 1
        print("total student: " + str(self.students))
