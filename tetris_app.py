import pygame
from pygame.locals import *
from SceneManager import SceneManager, GameIntro

# Setup pygame engine
pygame.init()
flags = pygame.FULLSCREEN

# screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("pyThetris")

# Launch applications scene director that will handle different game status (splash intro, playing, game over, ...)
director = SceneManager(pygame, screen)
director.scene = GameIntro()
director.play()

# End
pygame.quit()