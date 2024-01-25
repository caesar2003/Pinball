from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

import functions.general as general
from functions.general import get_angle
import vars.setup as setup
from vars.setup import wall_group