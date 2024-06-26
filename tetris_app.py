import pygame
from pygame.locals import *
from Tetris import SceneManager
from Tetris.Scenes import GameIntro, Playing, GameOver
# Setup pygame engine
pygame.init()
flags = pygame.FULLSCREEN

#screen = pygame.display.set_mode((1024, 768), FULLSCREEN)
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("pyThetris")

# Launch applications scene director that will handle different game status (splash intro, playing, game over, ...)
director = SceneManager(screen)
# director.scene = GameIntro()
# director.play()
director.scene = Playing()
director.play()
director.scene = GameOver()
director.play()

# End
pygame.quit()