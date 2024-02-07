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
import functions.score as sc
from vars.setup import clock
from vars.setup import screen, bg, bg_rect, width, height
from vars.setup import wall_group, ball_group, circle_group, flipper_group
def event(flipper_right, flipper_left, shot):
    for event in pygame.event.get():
            # close game
            if event.type == pygame.QUIT:
                system.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    system.close()
                if event.key == pygame.K_d:
                    flipper_right.rotating = True
                if event.key == pygame.K_a:
                    flipper_left.rotating = True
                if event.key == pygame.K_SPACE:
                    shot.pressed = True
                if event.key == pygame.K_r:
                    sc.new_ball()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    flipper_right.rotating = False
                if event.key == pygame.K_a:
                    flipper_left.rotating = False
                if event.key == pygame.K_SPACE:
                    shot.pressed = False