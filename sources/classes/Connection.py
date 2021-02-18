import pygame
from tools import SpriteLists


class Connection(pygame.sprite.Sprite):
    def __init__(self, src, dest):
        super().__init__()
        SpriteLists.line_list.append((src, dest))
