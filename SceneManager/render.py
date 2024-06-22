import pygame.draw

from SinglePlayer import SinglePlayer

block_width = 20
delta_x = 300
delta_y = 100
class Render():

    def __init__(self, pygame, screen):
        self.__pygame = pygame
        self.__screen = screen

    def draw(self, partita: SinglePlayer):
        tetromino = partita.current
        next_tetromino = partita.next

        # cancella tutto
        self.__screen.fill("black")

        # Disegna il "campo da gioco"
        y = 0
        for row in partita.playground.data:
            x = 0
            for el in row:
                if el != 0:
                    fill_color = self._get_tetromino_fill_color(el)
                    rect_x = delta_x + (x * block_width)
                    rect_y = delta_y + (y * block_width)
                    pygame.draw.rect(self.__screen, fill_color,  (rect_x, rect_y, (block_width), (block_width)), 0)
                x += 1
            y += 1

        # Disegna il tetramino corrente
        fill_color = self._get_tetromino_fill_color(tetromino.id)
        tetramino_state = tetromino.get_state()
        for y in range(4):
            for x in range(4):
                if tetramino_state[y][x] != 0:
                    rect_x = delta_x + (x * block_width) + (tetromino.x * block_width)
                    rect_y = delta_y + (y * block_width) + (tetromino.y * block_width)
                    pygame.draw.rect(self.__screen, fill_color, (rect_x, rect_y, (block_width - 1), (block_width - 1)), 0)


        # Disegna il prossimo tetramino
        fill_color = self._get_tetromino_fill_color(next_tetromino.id)
        tetramino_prossimo_state = next_tetromino.get_state()
        for y in range(4):
            for x in range(4):
                if tetramino_prossimo_state[y][x] != 0:
                    rect_x = delta_x + (x * block_width) + 500
                    rect_y = delta_y + (y * block_width)
                    pygame.draw.rect(self.__screen, fill_color,(rect_x, rect_y, (block_width - 1), (block_width - 1)), 0)


    def _get_tetromino_fill_color(self, id):
        match id:
            case 1:
                return (0, 255, 255)
            case 2:
                return (0, 0, 255)
            case 3:
                return (255, 165, 0)
            case 4:
                return (255, 215, 0)
            case 5:
                return (50, 205, 50)
            case 6:
                return (148, 0, 211)
            case 7:
                return (220, 20, 60)
            case 255:
                return "white"
