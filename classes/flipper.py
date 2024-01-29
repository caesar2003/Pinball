from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

import functions.general as general
from functions.general import get_angle
import vars.setup as setup
from vars.setup import wall_group, flipper_group
from classes.vectors import Vector


# definition of the class
class Flipper(pygame.sprite.Sprite):
    '''
    the class for the flipper
    subclass of pygame.sprite.Sprite to make it compatible with pygame groups
    
    object attributes:
    coords (numpy array containing floats): coordinates of the walls corners
    angles (float): angles of the surfaces of the wall
    index (int): some index number to log the order of the walls (idk if this will be usefull sometime)
                                                this will only exist if arg group == True
    self.rotations (list containing Wall objects): contains all needed rotations for collisions function
                                                this will only exist if arg group == True

    dunder methods:
    __init__: initiation method of the class
    __str__: properties of the wall

    other methods:
    update: does all the updates of the wall
    '''

    def __init__(self, rot_point, radius,direction, start_angle= np.pi, stop_angle =3*np.pi/2, group = True):
        '''
        initiation of a flipper object
        
        args:
        lists or numpy arrays with two elements: coordinates of its corners
        group (bool): True on default, if True some extra stuff will be performed:
                    Wall is added to wall_group
                    Wall gets an index
                    Wall gets rotated copies
        
        returns: None

        raises:
        TypeError if args are not lists or numpy arrays
        '''

        # check for type of args
        
        super().__init__()
        if isinstance(rot_point, tuple) or isinstance(rot_point, list) or isinstance(rot_point, np.ndarray):
            self.coords = Vector(rot_point[0], rot_point[1])
        #if isinstance(end_point, tuple) or isinstance(end_point, list) or isinstance(end_point, np.ndarray):
            #self.coords_end = Vector(end_point[0], end_point[1])

        self.radius = radius
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.current_angle = start_angle
        self.coords_end = Vector(self.coords.x +self.radius * np.cos(self.start_angle),self.coords.y+ self.radius * np.sin(self.start_angle))
        self.rotating = False
        self.speed = np.pi/50
        self.direction = direction

        if group:
            flipper_group.add(self)
            self.index = len(flipper_group) - 1

    
    def __str__(self):
        '''
        returns properties of the wall
        '''
        return f'\
            coordinates:\n {self.coords}\n\n\
            angles:\n {self.angles}\n'

    def move(self):
        '''
        move the ball and update its velocity
        checks for collisions before (TODO)

        returns: None
        '''
        if self.rotating==True and self.direction==True:
            self.current_angle += self.speed
            if self.current_angle > self.stop_angle:
                self.current_angle = self.stop_angle
        elif  self.rotating == False and self.direction == True:
            self.current_angle -= self.speed
            if self.current_angle < self.start_angle:
                self.current_angle = self.start_angle
        elif self.rotating == True and self.direction == False:
            self.current_angle -= self.speed
            if self.current_angle < self.stop_angle:
                self.current_angle = self.stop_angle
        elif self.rotating == False and self.direction == False:
            self.current_angle += self.speed
            if self.current_angle > self.start_angle:
                self.current_angle = self.start_angle
        
        self.coords_end = Vector(self.coords.x +self.radius * np.cos(self.current_angle),self.coords.y+ self.radius * np.sin(self.current_angle))
 
    def update(self):
        '''
        does all the logic for the walls:
        draw

        returns: None
        '''
        self.move()
        pygame.draw.line(setup.screen, 'black', self.coords.values, self.coords_end.values, 5)

    