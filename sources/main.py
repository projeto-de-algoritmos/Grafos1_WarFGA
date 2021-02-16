import pygame
from tools import SpriteLists, Images, GenerateTable
from classes import Graph

pygame.init()
graph = Graph.Graph()
windowSizeX = 800
windowSizeY = 600
mainScreen = pygame.display.set_mode((windowSizeX, windowSizeY))

onMode = True


pygame.display.set_caption("Graph")
pygame.display.set_icon(Images.icon)

GenerateTable.createTable(graph)

# graph.print_graph()
#selectedNode = Node(32, 32)
selected = None

while onMode:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            onMode = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            empty_clicked_sprites = [
                s for s in SpriteLists.empty_list if s.rect.collidepoint(pos)]
            for sprite in empty_clicked_sprites:
                sprite.addStudent()

    mainScreen.fill((100, 30, 150))
    SpriteLists.all_sprites_list.draw(mainScreen)

    pygame.display.update()
