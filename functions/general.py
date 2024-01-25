# imports
import numpy as np
import pygame

# functions
def screen_bg(screen, bg):
    '''
    adjusts the background to the proportions of the screen
    
    args:
    screen (pygame surface): the var of the screen (usually the arg you put in is named "screen")
    bg (pygame surface): the var of the background you want to have

    returns: None
    '''

    s_width, s_height = screen.get_width(), screen.get_height() # get the proportions of the screen
    bg = pygame.transform.scale(bg, (s_width, s_height)) # background scaling
    screen.blit(bg, (0, 0)) # draws the image


def get_angle(*args):
    '''
    gets the angle of a line connecting two coordinates

    args:
    tuples, lists or np.arrays: two coordinates

    returns:
    angle: angle of the line connecting the coordinates
    
    raises:
    IndexError (not sure what error to raise here) if more or less than 2 arguments given
    TypeError if given arguments are not from type tuple, list or numpy array
    '''

    #errors
    if not len(args) == 2:
        raise IndexError('there are exactly two arguments to be given') # not sure what error to raise here
    for element in args:
        if not (isinstance(element, tuple) or isinstance(element, list) or isinstance(element, np.ndarray)):
            raise TypeError(f'arguments to be given have to be from type tuple, list or numpy.ndarray but are {type(args[0])} and {type(args[1])}')
    
    #the function
    p1, p2 = args
    
    if np.all(p1 == p2): # case of same coordinates
        angle = 0
    elif p1[0] == p2[0]: # case of same x coordinate 
        angle = np.pi / 2
    else: # other cases
        angle = np.arctan((p2[1] - p1[1]) / (p2[0] - p1[0]))

    # keep the angles positive (between 0 and pi or between 0 and 180°)
    if angle < 0:
        angle += np.pi

    return angle


def distance(p1, p2):
    '''
    returns the distance between two points

    args:
    p1 (tuple, list or numpy.ndarray): first point
    p2 (tuple, list or numpy.ndarray): second point
    arguments must contain 2 elements each: x coordinate first, then y coordinate

    returns:
    float: distance between the two points
    '''

    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)