# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

from classes.vectors import Vector

# gravity as vector
gravity = Vector(0, 0.15)