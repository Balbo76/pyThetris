import pygame
from Tetris.Abstract.scene_interface import Scene
from .render import Render
from pygame.locals import *
from Tetris.PlayerGame import PlayerGame

class Playing(Scene):
    def __init__(self):
        super().__init__()

    def run(self, screen):

        clock = pygame.time.Clock()
        graphicsRender = Render(screen)
        partita = PlayerGame()


        key_pressed = {
            K_SPACE: False,
            K_LEFT: False,
            K_RIGHT: False,
            K_DOWN: False,
            K_ESCAPE: False,
        }
        done = False
        i = 0

        while not done:
            i += 1
            fps = clock.get_fps()

            for ev in pygame.event.get([KEYDOWN, KEYUP, QUIT], True):
                if ev.type == pygame.QUIT:
                    quit()
                elif ev.type == KEYDOWN and ev.key in [K_SPACE, K_LEFT, K_RIGHT, K_DOWN, K_ESCAPE]:
                    key_pressed[ev.key] = True
                elif ev.type == KEYUP and ev.key in [K_SPACE, K_LEFT, K_RIGHT, K_DOWN, K_ESCAPE]:
                    key_pressed[ev.key] = False

            if (i % 10) == 0:
                if key_pressed[K_SPACE]:
                    partita.rotate()
                if key_pressed[K_LEFT]:
                    partita.move_left()
                if key_pressed[K_RIGHT]:
                    partita.move_right()
                if key_pressed[K_DOWN]:
                    partita.move_down()
                if key_pressed[K_ESCAPE]:
                    quit()

            if (i % 60) == 0:
                partita.tick()

            if (i % 120) == 0:
                i = 0

            if partita.gameOver:
                done = True

            graphicsRender.draw(partita, fps)
            pygame.display.flip()
            clock.tick(60)
