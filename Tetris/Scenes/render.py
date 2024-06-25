import pygame
from Tetris.PlayerGame import PlayerGame

block_width = 20
delta_x = 150
delta_y = 100
class Render():

    def __init__(self, screen):
        self.screen = screen

    def draw(self, partita: PlayerGame, fps):
        tetromino = partita.current
        next_tetromino = partita.next

        self.screen.fill("black") # cancella la schermata precedente
        self._draw_playground(partita.playground)
        self._draw_current(tetromino)
        self._draw_next(next_tetromino)
        self._draw_linee_fatte(partita.lineeFatte)
        self._draw_fps(fps)

    def _draw_playground(self, playground):
        # Disegna il "campo da gioco"
        y = 0
        for row in playground.data:
            x = 0
            for el in row:
                if el != 0:
                    fill_color = self._get_tetromino_fill_color(el)
                    rect_x = delta_x + (x * block_width)
                    rect_y = delta_y + (y * block_width)
                    pygame.draw.rect(self.screen, fill_color, (rect_x, rect_y, (block_width), (block_width)), 0)
                x += 1
            y += 1

    def _draw_current(self, tetromino):
        # Disegna il tetramino corrente
        fill_color = self._get_tetromino_fill_color(tetromino.id)
        tetramino_state = tetromino.get_state()
        for y in range(4):
            for x in range(4):
                if tetramino_state[y][x] != 0:
                    rect_x = delta_x + (x * block_width) + (tetromino.x * block_width)
                    rect_y = delta_y + (y * block_width) + (tetromino.y * block_width)
                    pygame.draw.rect(self.screen, fill_color, (rect_x, rect_y, (block_width - 1), (block_width - 1)), 0)

    def _draw_next(self, next_tetromino):
        # Disegna il prossimo tetramino
        fill_color = self._get_tetromino_fill_color(next_tetromino.id)
        tetramino_prossimo_state = next_tetromino.get_state()
        for y in range(4):
            for x in range(4):
                if tetramino_prossimo_state[y][x] != 0:
                    rect_x =  (x * block_width) + 600
                    rect_y =  (y * block_width) + 100
                    pygame.draw.rect(self.screen, fill_color, (rect_x, rect_y, (block_width - 1), (block_width - 1)), 0)

    def _draw_linee_fatte(self, linee_fatte):
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text_surface = font.render( "Totale: " + str(linee_fatte), True, (255, 255, 255))
        self.screen.blit(text_surface, (600, 200))

    def _draw_fps(self, fps = "0"):
        fps_text = str(f"fps: {fps:.2f}")
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text_surface = font.render(fps_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (600, 300))
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
