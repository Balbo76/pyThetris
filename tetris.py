
import pygame
from pygame.locals import *
from os.path import join
from game import Game

partita = Game()

print(partita.tetramino_corrente)


# --- Inizializzazione
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tetris")
clk = pygame.time.Clock()
pressed = None


sound_laser = pygame.mixer.Sound(join("assets","sounds","Drum.wav"))

# --- Ciclo principale
done = False
while not done:
	# --- Ciclo degli eventi
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			done = True
		elif ev.type == KEYDOWN and ev.key in (K_LEFT, K_RIGHT):
			pressed = ev.key
		elif ev.type == KEYUP and ev.key == pressed:
			pressed = None

	if pressed == K_LEFT:
		print('LEFT')
		sound_laser.play()
	elif pressed == K_RIGHT:
		print('RIGHT')

	pygame.display.flip()
	clk.tick(30)

# --- Uscita
pygame.quit()