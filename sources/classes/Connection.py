import pygame
from tools import SpriteLists


class Connection(pygame.sprite.Sprite):
    def __init__(self, width, height, orientation):
        super().__init__()
        self.image = pygame.image.load(
            './assets/'+orientation+'.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        SpriteLists.connection_list.add(self)
        SpriteLists.all_sprites_list.add(self)
