# imports

import pygame
import numpy as np

from classes.ball import Ball
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
import functions.sound as sd
#from functions.score import save_data
import vars.const as const
import vars.setup as setup
from vars.setup import clock
from vars.setup import screen, bg, bg_rect, width, height
from vars.setup import ball_group, circle_group, flipper_group, shot_group, line_group
# import classes.vectors


# initialize pygame
pygame.init()

###Flipper############################
flipper_right = Flipper([width-15-50-5-125,height-100], 100,True, np.pi, 3*np.pi/2)
flipper_left = Flipper([10+125,height-100], 100,False,0, -np.pi/2)
#####Hintergrund um Feld####
rect([400, 100], 50, 50)
Line([10,10], [width-10,10])
Line([width-10,10], [width-10,height-10])
Line([10,10], [10,height-10])
######Abschuss rechts#################
shot = Shot([width-15-50, height-18],[width-15,height-18], 10, 50)
Line([width-15-50-5,height-10], [width-15-50-5,height/3])
##########################################
Line([width*0.75, 10], [width-10, height*0.25])##########rechts oben schräg
###########Kreise######################
Circle(375,300, 50, [0,0])
Circle(250,150, 50, [0,0])
Circle(125,300, 50, [0,0])
Circle(250,400, 30, [1,0])
#####schräge unten neben Flipper#####
Line([width-15-50-5,height-300], [width-15-50-5-125,height-100])
Line([10,height-300], [10+125,height-100])
sd.background_music()
while True:
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
        circle_group.update()
        flipper_group.update()
        shot_group.update()
        line_group.update()
        write_highscore(save_high)
        lives = new_ball_spawn(ball_group, lives) #spawns a new ball when old is gone
        current_score, lives= score(current_score, lives)

        # update screen
        pygame.display.flip()
        clock.tick(setup.fps)
        if lives == 0:
            break
