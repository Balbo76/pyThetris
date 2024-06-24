import pygame
from .scene_interface import Scene
from .render import Render
from pygame.locals import *
from os.path import join
from PlayerGame import PlayerGame

class Playing(Scene):
    def __init__(self):
        super().__init__()

    def run(self, screen):

        clock = pygame.time.Clock()
        graphicsRender = Render(screen)
        partita = PlayerGame()
        pressed = None
        done = False
        i = 0

        while not done:
            i += 1
            fps = clock.get_fps()
            if (i % 60) == 0:
                partita.tick()

            if (i % 4) == 0:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        quit()
                    elif ev.type == KEYDOWN and ev.key in [K_SPACE, K_LEFT, K_RIGHT, K_DOWN, K_ESCAPE]:
                        pressed = ev.key
                    elif ev.type == KEYUP and ev.key == pressed:
                        pressed = None

                if pressed == K_SPACE:
                    partita.rotate()
                if pressed == K_LEFT:
                    partita.move_left()
                if pressed == K_RIGHT:
                    partita.move_right()
                if pressed == K_DOWN:
                    partita.move_down()
                if pressed == K_ESCAPE:
                    quit()

                pressed = None


            if (i % 90) == 0:
                i = 0

            if partita.gameOver:
                done = True

            graphicsRender.draw(partita, fps)
            pygame.display.flip()
            clock.tick(60)
