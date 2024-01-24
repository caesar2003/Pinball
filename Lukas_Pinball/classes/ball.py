# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

import vars.const as const
import vars.setup as setup
from vars.setup import ball_group
from classes.vectors import Vector


# definition of the
#  class
class Ball(pygame.sprite.Sprite):
    '''
    Balls, theres nothing more to say, its just the class for the Balls in the game
    subclass of pygame.sprite.Sprite to make it compatible with pygame groups
    
    class attributes:
    gravity: acceleration of the ball in y+ direction (downwards)

    object attributes:
    coords (Vector)(2-dimensional): coordinates of the Ball center
    radius (int or float): size of the ball
    speed (Vector)(2-dimensional): speed of the Ball
    index (int): some index number to log the order of the walls (idk if this will be usefull sometime)
                                                this will only exist if arg group == True

    dunder methods:
    __init__: initiation method of the class
    __str__: attributes of the ball

    other methods:
    update: does all the logical and graphical updates of the ball
    '''

    # global gravity to all balls (maybe this will become a object specific attribute later)
    gravity = const.gravity

    def __init__(self, x, y, radius = setup.ball_rad, group = True):
        '''
        initiation of a ball object

        args:
        x, y: initial coordinates of the ball
        radius: (initial) radius of the ball
        '''

        super().__init__()

        self.coords = Vector(x, y)
        self.radius = radius

        self.speed = Vector(0, 0)

        if group:
            ball_group.add(self)
            self.index = len(ball_group) - 1


    def __str__(self):
        '''
        returns attributes of the ball
        '''
        return f'\
            Ball with positional vector:\n{self.coords}\n\n\
            velocity:\n{self.speed}\n\n\
            gravity:\n{self.gravity}\n\n\
            radius: {self.radius}\n\n\
            index: {self.index}'


    def draw(self):
        pygame.draw.circle(setup.screen, 'black', self.coords.values, self.radius, width = 2)
        pygame.draw.circle(setup.screen, 'white', self.coords.values, self.radius - 2)
        pygame.draw.circle(setup.screen, 'blue', self.coords.values, self.radius - 18)
        pygame.draw.circle(setup.screen, 'black', self.coords.values, 4)


    def move(self):
        '''
        move the ball and update its velocity
        checks for collisions before (TODO)

        returns: None
        '''
        self.speed += self.gravity
        self.coords += self.speed


    def update(self):
        '''
        does all the logical and graphical updates for the ball:
        
        movement updates
        drawing

        
        returns: None
        '''
        
        self.move()
        self.draw()

        # TODO:
        # movement updates (to be updated (no thats not intended))
        # collision checks

