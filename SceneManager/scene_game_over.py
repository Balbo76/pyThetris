from .scene_interface import Scene
from pygame.locals import *
from os.path import join


class GameOver(Scene):
    def run(self, screen):

        surf_gameover = pygame.image.load(join("assets", "images", "gameover.bmp"))
        rect_gameover = surf_gameover.get_rect()
        rect_gameover.update(100 ,100, 1024, 768)
        screen.blit(surf_gameover, rect_gameover )

        clk = pygame.time.Clock()
        pressed = None
        done = False
        while not done:
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
