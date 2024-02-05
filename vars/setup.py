# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame


### SETUP
# time
clock = pygame.time.Clock()
fps = 60

# screen
width = 600
height = 700
screen = pygame.display.set_mode((width, height))#, pygame.RESIZABLE
bg = pygame.image.load('graphics/bkg.jpg')
bg_rect = bg.get_rect(topleft = (0, 0))

# groups
wall_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()
circle_group = pygame.sprite.Group()
flipper_group = pygame.sprite.Group()
shot_group = pygame.sprite.Group()
line_group = pygame.sprite.Group()

#ball
ball_rad = 18