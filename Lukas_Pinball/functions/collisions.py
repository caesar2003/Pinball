# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np

from classes.wall import Wall


# functions

def rotate_wall(wall):
    '''
    rotates a wall to make one angle 0 at a time

    args:
    wall (class: Wall): The wall to be rotated

    yields:
    a new wall for every angle
    
    optional TODO to speed up the code:
    dont rotate the whole wall but instead just the side to be turned to zero
    '''

    for angle in wall.angles:
        new_coords = []
        
        for i in range(len(wall.coords)):
            old_coords = np.array([wall.coords[i][0], wall.coords[i][1]])
            rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            new_coords += [np.dot(old_coords, rotation).tolist()]
            
        yield Wall(*new_coords, group = False)


def col_ball_wall(ball, wall):
    '''
    checks for collision of ball and wall
    
    args:
    ball (class: Ball): the ball to check
    wall (class: Wall): the wall to check
    
    returns:
    bool: true if collision is happening, else false
    '''

    # TODO:
    # rotate wall for each side (rotate_wall is defined)
    # check for collision for each side


    

