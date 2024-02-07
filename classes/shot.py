from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

import functions.general as general
from functions.general import get_angle, distance
import vars.setup as setup
from vars.setup import wall_group, flipper_group, shot_group
from classes.vectors import Vector


# definition of the class
class Shot(pygame.sprite.Sprite):
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

    def __init__(self, start_point, end_point,speed, distance, group = True):
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
        if isinstance(start_point, tuple) or isinstance(start_point, list) or isinstance(start_point, np.ndarray):
            self.coords = Vector(start_point[0], start_point[1])
        if isinstance(end_point, tuple) or isinstance(end_point, list) or isinstance(end_point, np.ndarray):
            self.coords_end = Vector(end_point[0], end_point[1])
        self.start_coords = [self.coords, self.coords_end]
        self.speed = speed
        self.distance = distance
        self.pressed = False
        self.nv = Vector(0,-1)
        self.check_velocity= False
        if group:
            shot_group.add(self)
            self.index = len(shot_group) - 1

    
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
        if self.pressed:
            self.coords += Vector(self.nv.x*self.speed, self.nv.y*self.speed)
            self.coords_end += Vector(self.nv.x*self.speed, self.nv.y*self.speed)
            self.check_velocity = True
            if distance([self.start_coords[0].x,self.start_coords[0].y], [self.coords.x, self.coords.y]) >= self.distance:
                self.check_velocity = False
                self.coords = Vector(self.start_coords[0].x+self.nv.x*self.distance, self.start_coords[0].y+self.nv.y*self.distance)
                self.coords_end= Vector(self.start_coords[1].x+self.nv.x*self.distance, self.start_coords[1].y+self.nv.y*self.distance)
        else:
            self.coords -= Vector(self.nv.x*self.speed, self.nv.y*self.speed)
            self.coords_end -= Vector(self.nv.x*self.speed, self.nv.y*self.speed)
            self.check_velocity = False
            if distance([self.start_coords[0].x+self.nv.x*self.distance,self.start_coords[0].y+self.nv.y*self.distance], [self.coords.x, self.coords.y])- self.distance >=0:
                self.check_velocity = False
                self.coords = self.start_coords[0]
                self.coords_end = self.start_coords[1]
        
    def update(self):
        '''
        does all the logic for the walls:
        draw

        returns: None
        '''
        print(self.speed)
        self.move()
        pygame.draw.line(setup.screen, 'black', self.coords.values, self.coords_end.values, 5)

    