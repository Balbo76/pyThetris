import pygame
from pygame.locals import *

class KeyboardHandler:

    def __init__(self, key_to_monitor):
        self.key_pressed = {}
        for key in key_to_monitor:
            self.key_pressed[key] = False

    def handle(self, pump):
        for ev in pygame.event.get([KEYDOWN, KEYUP, QUIT], pump):
            if ev.type == pygame.QUIT:
                quit()
            elif ev.type == KEYDOWN and ev.key in [K_SPACE, K_LEFT, K_RIGHT, K_DOWN, K_ESCAPE]:
                self.key_pressed[ev.key] = True
            elif ev.type == KEYUP and ev.key in [K_SPACE, K_LEFT, K_RIGHT, K_DOWN, K_ESCAPE]:
                self.key_pressed[ev.key] = False

    def get_pressed_keys(self):
        return self.key_pressed