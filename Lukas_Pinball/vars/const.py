# imports
# if __name__ == "__main__":

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame

# gravity as radial coordinates 
gravity = 0.15
gravity_angle = -np.pi / 2