# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

import functions.collisions as coll
import vars.const as const
import vars.setup as setup
from vars.setup import ball_group, wall_group, circle_group, flipper_group
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
    rotate: returns a copy of the ball with rotated coordinates by a given angle
    '''

    # global gravity to all balls (maybe this will become a object specific attribute later)
    gravity = const.gravity
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
            ball_group.add(self)
            self.index = len(ball_group) - 1

        self.test = True

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
        for wall in wall_group:
            is_colliding, coll_angle = coll.col_ball_wall(self, wall)
            if is_colliding and self.test:
                self.speed.rotate(2*-(coll_angle - self.speed.angle))
                
        for circle in circle_group:
            is_colliding, coll_angle, col_deep = coll.col_ball_circle(self, circle)
            if is_colliding and self.test:
                    #self.coords = Vector(self.coords.x + col_deep*np.cos(coll_angle), self.coords.y + col_deep*np.sin(coll_angle))
                    self.speed.rotate(2*-(coll_angle - self.speed.angle))

        for flipper in flipper_group:
            is_colliding, coll_angle = coll.col_ball_flipper(self, flipper)
            if is_colliding and self.test:
                    #self.coords = Vector(self.coords.x + col_deep*np.cos(coll_angle), self.coords.y + col_deep*np.sin(coll_angle))
                    #self.speed.rotate(2*-(coll_angle - self.speed.angle))
                    print(True)


        self.draw()

        # TODO:
        # movement updates (to be updated (no thats not intended))
        # collision checks


    def rotate(self, angle):
        '''
        rotate the coordinates of a ball by a given angle

        args:
        ball (class: Ball): The ball of which the coordinates will be rotated
        angle (in rad): The angle to rotate the coordinates

        returns:
        a new instance of class Ball
        '''

        old_coords = self.coords.values # coordinates as numpy array (see: classes.vectors)
        old_speed = self.speed.values
        rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) # rotation matrix (clockwise due to the positive y direction being downwards)
        new_coords = np.dot(old_coords, rotation).tolist()
        new_speed = np.dot(old_speed, rotation).tolist()

        return Ball(*new_coords, self.radius, speed = new_speed, group = False)



