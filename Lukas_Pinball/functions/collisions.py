# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np

# from classes.ball import Ball
# from classes.wall import Wall
import vars.setup as setup


# functions

# def rotate_wall(wall):
#     '''
#     rotates a wall to make one angle 0 at a time

#     args:
#     wall (class: Wall): The wall to be rotated

#     yields:
#     a new instance of class Wall for each angle


#     optional TODO to speed up the code:
#     dont rotate the whole wall but instead just the side to be turned to zero
#     '''

#     for angle in wall.angles:
#         new_coords = []
        
#         for i in range(len(wall.coords)):
#             old_coords = np.array([wall.coords[i][0], wall.coords[i][1]])
#             rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) # rotation matrix (clockwise due to the positive y direction being downwards)
#             new_coords += [np.dot(old_coords, rotation).tolist()]
            
#         yield Wall(*new_coords, group = False)

# testing of rotate_wall
# a = Wall([10, 0], [0, 0], [5, 5], group = False)
# a_rot = rotate_wall(a)
# for i in range(3):
#     print(next(a_rot).angles)


# def rotate_ball(ball, angle):
#     '''
#     rotate the coordinates of a ball by a given angle

#     args:
#     ball (class: Ball): The ball of which the coordinates will be rotated
#     angle (in rad): The angle to rotate the coordinates

#     returns:
#     a new instance of class Ball
#     '''

#     old_coords = ball.coords.values # coordinates as numpy array (see: classes.vectors)
#     rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) # rotation matrix (clockwise due to the positive y direction being downwards)
#     new_coords = np.dot(old_coords, rotation).tolist()

#     return Ball(*new_coords, ball.radius, group = False)

# testing of rotate_ball
# b = Ball(1, 0, setup.ball_rad)
# print(rotate_ball(b, np.radians(90)).coords)


def col_ball_wall(ball, wall):
    '''
    checks for collision of ball and wall
    
    args:
    ball (class: Ball): the ball to check
    wall (class: Wall): the wall to check
    
    returns:
    bool: true if collision is happening, else false
    angle: the angle of the collision (vom Lot aus (TODO: Übersetzen))
    '''

    collision = False

    for i in range(len(wall.angles)):
        angle = wall.angles[i]

        rot_ball = ball.rotate(angle)
        rot_wall = wall.rotations[i]

        j = i + 1
        if j == len(wall.angles):
            j = 0
        
        
        if rot_wall.coords[i][0] <= rot_ball.coords.x <= rot_wall.coords[j][0] or rot_wall.coords[j][0] <= rot_ball.coords.x <= rot_wall.coords[i][0]:
            if abs(rot_ball.coords.y - rot_wall.coords[i][1]) <= ball.radius:
                return True # TODO: return angle, check for remaining distance

        # TODO:
        # check for lines between edges (WIP)
        # check for edges
        # change variable 'collision' to 'True' if a collision is happening
        # calculate the angle if a collision is happening
        # break the loop if a collision is happening








    

