# imports

import pygame
import numpy as np

from classes.ball import Ball
from classes.wall import Wall
import functions.collisions as col
import functions.general as general
import functions.system as system
import vars.const as const
import vars.setup as setup
from vars.setup import clock
from vars.setup import screen, bg, bg_rect, width, height
from vars.setup import wall_group, ball_group
# import classes.vectors


# initialize pygame
pygame.init()

# preparation
Ball(width / 2, height / 2 - 100)
Wall([160, height / 2], [width - 100, height - 200], [width / 2, height - 50])
Wall([500, 0], [700, 0], [650, 700])



### GAME
while True:

    ## Event Loop
    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT:
            system.close()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                system.close()
    
    ## Logic
    general.screen_bg(screen, bg)
    ball_group.update()
    wall_group.update()

    # update screen
    pygame.display.flip()
    clock.tick(setup.fps)

