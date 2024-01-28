from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from classes.wall import Wall

import numpy as np
import pygame

import functions.general as general
from functions.general import get_angle
import vars.setup as setup
from vars.setup import wall_group

def rect(center, width, height):
    top = Wall([center-width/2, center+height/2], [center+width/2, center+height/2])
    right = Wall([center+width/2, center+height/2], [center+width/2, center-height/2])
    bottom = Wall([center+width/2, center-height/2], [center-width/2, center-height/2])
    left = Wall([center-width/2, center-height/2], [center-width/2, center+height/2])