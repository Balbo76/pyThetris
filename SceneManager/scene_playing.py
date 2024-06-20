from .scene_interface import Scene
from .render import Render
from pygame.locals import *
from os.path import join
from Game import Game

class Playing(Scene):
    def run(self, pygame, screen):

        render = Render(pygame, screen)
        partita = Game()

        clk = pygame.time.Clock()
        pressed = None
        done = False
        while not done:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    done = True
                elif ev.type == KEYDOWN and ev.key in [K_SPACE, K_LEFT, K_RIGHT, K_DOWN]:
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
                pass


            render.render(partita)
            pygame.display.flip()
            clk.tick(30)