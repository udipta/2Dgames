import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
clock = pygame.time.Clock()

windowWidth = 640
windowHeight = 480

surface = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('Pygame Shapes!')

squareX = 0
squareY = 0


while True:

	surface.fill((0,0,0))

	# Drawing Shapes in Time and Space
	pygame.draw.rect(surface, (255,0,0), (random.randint(0, windowWidth), random.randint(0, windowHeight), 10, 10 ) )

	for event in GAME_EVENTS.get():

		if event.type == GAME_GLOBALS.QUIT:

			pygame.quit()

			sys.exit()

	clock.tick(60)
	pygame.display.update()
