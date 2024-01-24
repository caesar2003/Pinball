# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

import functions.general as general
from functions.general import get_angle
import vars.setup as setup
from vars.setup import wall_group


# definition of the class
class Wall(pygame.sprite.Sprite):
    '''
    the class for the walls
    subclass of pygame.sprite.Sprite to make it compatible with pygame groups
    
    object attributes:
    coords (numpy array containing floats): coordinates of the walls corners
    angles (float): angles of the surfaces of the wall
    index (int): some index number to log the order of the walls (idk if this will be usefull sometime)
                                                this will only exist if arg group == True
    self.rotations (list containing Wall objects): contains all needed rotations for collisions function
                                                this will only exist if arg group == True

    '''

    def __init__(self, *args, group = True):
        '''
        initiation of a wall object
        
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
        for element in args:
            if not (isinstance(element, list) or isinstance(element, np.ndarray)):
                raise TypeError(f'arguments have to be lists or numpy arrays but are {type(element)}')
        
        super().__init__()

        self.coords = np.array(args, dtype = float)


        self.angles = []
        temp_coords = np.append(self.coords, self.coords, axis = 0) # temporary variable including the coordinates twice

        for i in range(len(self.coords)):
            self.angles += [get_angle(temp_coords[i], temp_coords[i + 1])]
        self.angles = np.array(self.angles)

        del temp_coords # deletion of the temporary variable


        if group:
            wall_group.add(self)
            self.index = len(wall_group) - 1
            
            self.rotations = []
            for angle in self.angles:
                new_coords = []
        
                for i in range(len(self.coords)):
                    old_coords = np.array([self.coords[i][0], self.coords[i][1]])
                    rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) # rotation matrix (clockwise due to the positive y direction being downwards)
                    new_coords += [np.dot(old_coords, rotation).tolist()]
            
                self.rotations += [Wall(*new_coords, group = False)]


    def update(self):
        '''
        does all the logic for the walls:
        draw

        returns: None
        '''

        pygame.draw.lines(setup.screen, 'black', True, self.coords, 5)

    