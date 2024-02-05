# imports

import pygame
import numpy as np

#from classes.ball import Ball
from classes.wall import Wall
from classes.circle import Circle
from classes.flipper import Flipper
from classes.shot import Shot
from classes.line import Line
import functions.collisions as col
import functions.general as general
import functions.system as system
from functions.rectangle import rect
from functions.score import new_ball_spawn
from functions.events import event
from functions.score import score
from functions.score import highscores
from functions.score import write_highscore
#from functions.score import save_data
import vars.const as const
import vars.setup as setup
from vars.setup import clock
from vars.setup import screen, bg, bg_rect, width, height
from vars.setup import wall_group, ball_group, circle_group, flipper_group, shot_group, line_group
# import classes.vectors


# initialize pygame
pygame.init()

# preparation
flipper_right = Flipper([500,500], 200,True, np.pi, 3*np.pi/2)
flipper_left = Flipper([100,500], 200,False,0, -np.pi/2)
shot = Shot([100,100], [150, 100])

Line([10,0], [10,500])
Line([10,400], [100,500])
Line([500,500], [600,400])
Line([600,400], [600,0])
Line([0,0], [600,0])
#a = Wall([500, 500], [0,500])
#Wall([10, 10], [10, 400])
#Wall([10, 400], [300, 500])
#Wall([700, 10], [700, 400])
#Wall([700, 400], [10, 400])
#rect(250,50,50)
#Circle(400,200, 30, [1,0])
current_score=0
lives = 3
save_high=highscores()
### GAME
while True:

    ## Event Loop
    event(flipper_right, flipper_left, shot)     

    
    ## Logic
    general.screen_bg(screen, bg)
    ball_group.update()
    wall_group.update()
    circle_group.update()
    flipper_group.update()
    shot_group.update()
    line_group.update()
    write_highscore(save_high)
    current_score= score(current_score, lives)
    lives = new_ball_spawn(ball_group, lives) #spawns a new ball when old is gone
    


    # update screen
    pygame.display.flip()
    clock.tick(setup.fps)

