from .scene_interface import Scene
import pygame
from pygame.locals import *
from os.path import join


class GameIntro(Scene):

    def run(self, screen):

        surf_panda = pygame.image.load(join("assets", "images", "pyThetris.png"))
        rect_panda = surf_panda.get_rect()
        sound1 = pygame.mixer.Sound(join("assets", "sounds", "RAP_INTR.WAV"))

        screen.blit(surf_panda, rect_panda)
        sound1.play()

        clk = pygame.time.Clock()
        pressed = None
        # --- Ciclo principale
        done = False
        frame_number = 0
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
            frame_number += 1



