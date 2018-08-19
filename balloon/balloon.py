

import os
import pygame
from pygame.locals import *

pygame.display.init()
pygame.font.init()

pygame.display.set_caption("Balloon!  Don't hit the walls")

# is the game still going?
going = 1

screen = pygame.display.set_mode((600,400))

clock = pygame.time.Clock()


# fill the screen with red... for dramatic effect.
screen.fill((200,0,0))
pygame.display.flip()

def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pygame.image.load(i).convert_alpha()

terrain1 = pygame.transform.scale(load_image("terrain1.png"), (600, 400))
balloon = pygame.transform.scale(load_image("balloon.png"), (70, 70))

# create a mask for each of them.
terrain1_mask = pygame.mask.from_surface(terrain1, 50)
balloon_mask = pygame.mask.from_surface(balloon, 50)

# this is where the balloon, and terrain are.
terrain1_rect = terrain1.get_rect()
balloon_rect = balloon.get_rect()


# a message for if the balloon hits the terrain.
afont = pygame.font.Font(None, 16)
hitsurf = afont.render("Hit!!!  Oh noes!!", 1, (255,255,255))


last_bx, last_by = 0,0



# start the main loop.

while going:
    events = pygame.event.get()
    for e in events:
        if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
            going = 0
        if e.type == pygame.KEYDOWN:
            # move the balloon around, depending on the keys.
            if e.key in [K_LEFT]:
                balloon_rect.x -= 5
            if e.key in [K_RIGHT]:
                balloon_rect.x += 5
                
            if e.key in [K_UP]:
                balloon_rect.y -= 5
            if e.key in [K_DOWN]:
                balloon_rect.y += 5


    # see how far the balloon rect is offset from the terrain rect.
    bx, by = (balloon_rect[0], balloon_rect[1])
    offset_x = bx - terrain1_rect[0]
    offset_y = by - terrain1_rect[1]

    overlap = terrain1_mask.overlap(balloon_mask, (offset_x, offset_y))

    screen.fill((255,0,0))
    screen.blit(terrain1, (0,0))

    screen.blit(balloon, (balloon_rect[0], balloon_rect[1]) )

    if overlap:

        screen.blit(hitsurf, (0,0))


    pygame.display.flip()
    

    clock.tick(40)



pygame.quit()


