from .scene_interface import Scene
from .render import Render
from pygame.locals import *
from os.path import join
from SinglePlayer import SinglePlayer

class Playing(Scene):

    def run(self, pygame, screen):

        graphicsRender = Render(pygame, screen)
        partita = SinglePlayer()

        clk = pygame.time.Clock()
        pressed = None
        done = False
        i = 0

        while not done:
            i += 1
            
            if (i % 30) == 0:
                partita.tick()

            if (i % 2) == 0:
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
                    partita.move_down()


            if (i % 90) == 0:
                i = 0

            if partita.gameOver:
                done = True

            graphicsRender.draw(partita)
            pygame.display.flip()
            clk.tick(30)
