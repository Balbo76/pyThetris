import pygame
from Tetris.Abstract.scene_interface import Scene
from .render import Render
from pygame.locals import *
from Tetris.PlayerGame import PlayerGame
from ..keyboard_handler import KeyboardHandler

class Playing(Scene):
    def __init__(self):
        super().__init__()

    def run(self, screen):

        graphicsRender = Render(screen)
        partita = PlayerGame()

        key_event = KeyboardHandler([K_SPACE, K_LEFT, K_RIGHT, K_DOWN, K_ESCAPE])

        done = False
        i = 0

        while not done:
            fps = self.clock.get_fps()
            key_event.handle(True)

            if (i % 10) == 0:
                key_pressed = key_event.get_pressed_keys()
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

            if partita.gameOver:
                done = True

            graphicsRender.draw(partita, fps)
            pygame.display.flip()
            self.clock.tick(60)
            i += 1
            if (i % 60) == 0:
                i = 0
