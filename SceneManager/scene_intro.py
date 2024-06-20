from .scene_interface import Scene
from pygame.locals import *
from os.path import join


class GameIntro(Scene):
    def run(self, pygame, screen):

        surf_panda = pygame.image.load(join("assets", "images", "pyThetris.png"))
        rect_panda = surf_panda.get_rect()
        screen.blit(surf_panda, rect_panda)


        clk = pygame.time.Clock()
        pressed = None
        # --- Ciclo principale
        done = False
        while not done:
            # --- Ciclo degli eventi
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    done = True
                elif ev.type == KEYDOWN and ev.key == K_SPACE:
                    pressed = ev.key
                elif ev.type == KEYUP and ev.key == pressed:
                    pressed = None

            if pressed == K_SPACE:
                done = True

            pygame.display.flip()
            clk.tick(30)



