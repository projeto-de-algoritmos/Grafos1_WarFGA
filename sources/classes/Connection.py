import pygame as pg
from tools import SpriteLists


class Connection(pg.sprite.Sprite):
    def __init__(self, src, dest):
        super().__init__()
        SpriteLists.line_list.append((src, dest))