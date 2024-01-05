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
    coords (numpy array with floats): coordinates of the walls corners

    '''

    def __init__(self, *args, group = True):
        '''
        initiation of a wall object
        
        args:
        lists or numpy arrays with two elements: coordinates of its corners
        group (bool): True if wall has to be added to wall_group and be shown on the display, False if else
        
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
        if group:
            wall_group.add(self)

        self.angles = []
        temp_coords = np.append(self.coords, self.coords, axis = 0) # temporary variable including the coordinates twice

        for i in range(len(self.coords)):
            self.angles += [get_angle(temp_coords[i], temp_coords[i + 1])]
        self.angles = np.array(self.angles)

        del temp_coords # deletion of the temporary variable


    def update(self):
        '''
        does all the logic for the walls:
        draw

        returns: None
        '''
        pygame.draw.lines(setup.screen, 'black', True, self.coords, 5)

    