import pygame.draw

from Game import Game

block_width = 20
delta_x = 300
delta_y = 100
class Render():

    def __init__(self, pygame, screen):
        self.__pygame = pygame
        self.__screen = screen

    def render(self, partita: Game):
        playground = partita.playground.data
        tetramino = partita.tetramino_corrente

        y = 0
        for row in playground:
            x = 0
            for el in row:
                if el != 0:
                    rect_x = delta_x + (x * block_width)
                    rect_y = delta_y + (y * block_width)
                    pygame.draw.rect(self.__screen,"white",  (rect_x, rect_y, (block_width), (block_width)), 0)
                x += 1
            y += 1

        tetramino_state = tetramino.get_state()

        for y in range(4):
            for x in range(4):
                if tetramino_state[y][x] != 0:
                    rect_x = delta_x + (x * block_width) + (tetramino.x * block_width)
                    rect_y = delta_y + (y * block_width) + (tetramino.y * block_width)
                    pygame.draw.rect(self.__screen, "red", (rect_x, rect_y, (block_width - 2), (block_width - 2)), 0)




