# imports

import pygame
import numpy as np

from classes.ball import Ball
from classes.wall import Wall
from classes.circle import Circle
from classes.flipper import Flipper
import functions.collisions as col
import functions.general as general
import functions.system as system
from functions.rectangle import rect
import vars.const as const
import vars.setup as setup
from vars.setup import clock
from vars.setup import screen, bg, bg_rect, width, height
from vars.setup import wall_group, ball_group, circle_group, flipper_group
# import classes.vectors


# initialize pygame
pygame.init()

# preparation
Ball(650, 100 , speed= [0,-5])
Flipper([400,500], 50)


a = Wall([10, 10], [700, 10])
Wall([10, 10], [10, 400])
Wall([10, 400], [300, 500])
Wall([700, 10], [700, 400])
Wall([700, 400], [400, 500])
# print(str(a.rotations[0]))
# print(str(a.rotations[1]))
# print(str(a.rotations[2]))
rect(250,50,50)
Circle(400,200, 30, [1,0])


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
    circle_group.update()
    flipper_group.update()

    # update screen
    pygame.display.flip()
    clock.tick(setup.fps)

