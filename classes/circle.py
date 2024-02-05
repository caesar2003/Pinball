from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

import functions.collisions as coll
import vars.const as const
import vars.setup as setup
from vars.setup import ball_group, wall_group, circle_group
from classes.vectors import Vector


# definition of the
#  class
class Circle(pygame.sprite.Sprite):
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
    rotate: returns a copy of the ball with rotated coordinates by a given angle
    '''

    # global gravity to all balls (maybe this will become a object specific attribute later)
    #gravity = const.gravity
    # gravity = Vector(0, 0)

    def __init__(self, x, y, radius = setup.ball_rad, speed = None, group = True):
        '''
        initiation of a ball object

        args:
        x, y: initial coordinates of the ball
        radius: (initial) radius of the ball
        speed: initial speed of the ball
        group: determines if the ball is added to ball_group and gets an index

        raises:
        Type Error if argument speed is a not supported type
        '''

        super().__init__()

        self.coords = Vector(x, y)
        self.radius = radius

        if speed is None:
            self.speed = Vector(0, 0)
        elif isinstance(speed, tuple) or isinstance(speed, list) or isinstance(speed, np.ndarray):
            self.speed = Vector(speed[0], speed[1])
        elif isinstance(speed, Vector):
            self.speed = speed
        else:
            raise TypeError(f'type not supported (yet). Already supported types for argument "speed" are NoneType, tuple, list, numpy.ndarray and Vector. Given argument is from type {type(speed)}')

        if group:
            circle_group.add(self)
            self.index = len(circle_group) - 1

        self.test = True
        self.color = 'black'
    def __str__(self):
        '''
        returns attributes of the ball
        '''
        return f'\
            Ball with positional vector:\n{self.coords}\n\n\
            velocity:\n{self.speed}\n\n\
            gravity:\n{self.gravity}\n\n\
            radius: {self.radius}\n'


    def draw(self):
        pygame.draw.circle(setup.screen, self.color, self.coords.values, self.radius)


    def move(self):
        '''
        move the ball and update its velocity
        checks for collisions before (TODO)

        returns: None
        '''
        if self.coords.x >setup.width*0.75 or self.coords.x < setup.width*0.25:
            self.speed = Vector(-self.speed.x, self.speed.y)
        self.coords+= self.speed

    
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

    



