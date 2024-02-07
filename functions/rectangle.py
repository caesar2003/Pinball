from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from classes.line import Line

import numpy as np
import pygame

import functions.general as general
from functions.general import get_angle
import vars.setup as setup
from vars.setup import line_group

def rect(center, width, height):
    top = Line([center[0]-width/2, center[1]+height/2], [center[0]+width/2, center[1]+height/2], 'Blue')
    right = Line([center[0]+width/2, center[1]+height/2], [center[0]+width/2,center[1]-height/2], 'Blue')
    bottom = Line([center[0]+width/2, center[1]-height/2], [center[0]-width/2, center[1]-height/2], 'Blue')
    left = Line([center[0]-width/2, center[1]-height/2], [center[0]-width/2, center[1]+height/2], 'Blue')