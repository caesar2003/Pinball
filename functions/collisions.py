# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import math 

# from classes.ball import Ball
# from classes.wall import Wall
import vars.setup as setup
from functions.general import distance, get_angle
from classes.vectors import Vector

def col_ball_circle(ball, circle):
    '''
    checks for collision of ball and circle
    
    args:
    ball (class: Ball): the ball to check
    circle (class: Circle): the circle to check
    
    returns:
    bool: true if collision is happening, else false
    angle: the angle of the collision (vom Lot aus (TODO: Übersetzen))
    '''

    collision = False
    if distance(ball.coords.values, circle.coords.values) <= ball.radius + circle.radius:
        normal_vector= Vector(ball.coords.x -circle.coords.x, ball.coords.y -circle.coords.y)
        
        return True, normal_vector
    else:
        return False, 0

    
def col_ball_flipper(ball, flipper):
    '''
    checks for collision of ball and circle
    
    args:
    ball (class: Ball): the ball to check
    circle (class: Circle): the circle to check
    
    returns:
    bool: true if collision is happening, else false
    angle: the angle of the collision (vom Lot aus (TODO: Übersetzen))
    '''
    if distance(ball.coords.values, flipper.coords.values) <= ball.radius:
        closestx, closesty = flipper.coords_end.x, flipper.coords_end.y
        normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty )
        normal_vector_norm = Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
        abs_v = distance([closestx, closesty], flipper.coords.values)* flipper.speed
        v_vector = Vector(abs_v * normal_vector_norm.x, abs_v * normal_vector_norm.y)
        col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
        return True, normal_vector, v_vector, col_deep
    elif distance(ball.coords.values, flipper.coords_end.values) <= ball.radius:
        closestx, closesty = flipper.coords_end.x, flipper.coords_end.y
        normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty )
        normal_vector_norm = Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
        abs_v = distance([closestx, closesty], flipper.coords.values)* flipper.speed
        v_vector = Vector(abs_v * normal_vector_norm.x, abs_v * normal_vector_norm.y)
        col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
        return True, normal_vector, v_vector, col_deep
    
    line_len = distance(flipper.coords.values, flipper.coords_end.values)
    dot = ((ball.coords.x-flipper.coords.x)* (flipper.coords_end.x-flipper.coords.x)+ (ball.coords.y-flipper.coords.y)* (flipper.coords_end.y-flipper.coords.y))/line_len**2
    closestx=flipper.coords.x+ (dot*(flipper.coords_end.x-flipper.coords.x))
    closesty=flipper.coords.y+ (dot*(flipper.coords_end.y-flipper.coords.y))
    buffer = 0.1
    d1= distance([closestx, closesty], flipper.coords.values)
    d2= distance([closestx, closesty], flipper.coords_end.values)
    if(d1+d2 >= line_len-buffer and d1+d2 <= line_len+buffer):
        ball_to_line = distance(ball.coords.values, [closestx, closesty])
        if ball_to_line <= ball.radius:
            normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty)
            normal_vector_norm = Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
            abs_v = distance([closestx, closesty], flipper.coords.values)* flipper.speed
            v_vector = Vector(abs_v * normal_vector_norm.x, abs_v * normal_vector_norm.y)
            col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
            return True, normal_vector, v_vector, col_deep
    return False, 0, Vector(0,0), 0

def col_ball_line(ball, line):
    '''
    checks for collision of ball and circle
    
    args:
    ball (class: Ball): the ball to check
    circle (class: Circle): the circle to check
    
    returns:
    bool: true if collision is happening, else false
    angle: the angle of the collision (vom Lot aus (TODO: Übersetzen))
    '''
    if distance(ball.coords.values, line.coords.values) <= ball.radius:
        closestx, closesty = line.coords_end.x, line.coords_end.y
        normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty )
        col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
        return True,normal_vector, col_deep
    elif distance(ball.coords.values, line.coords_end.values) <= ball.radius:
        closestx, closesty = line.coords_end.x, line.coords_end.y
        normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty )
        col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
        return True, normal_vector, col_deep
    line_len = distance(line.coords.values, line.coords_end.values)
    dot = ((ball.coords.x-line.coords.x)* (line.coords_end.x-line.coords.x)+ (ball.coords.y-line.coords.y)* (line.coords_end.y-line.coords.y))/line_len**2
    closestx=line.coords.x+ (dot*(line.coords_end.x-line.coords.x))
    closesty=line.coords.y+ (dot*(line.coords_end.y-line.coords.y))
    buffer = 0.1
    d1= distance([closestx, closesty], line.coords.values)
    d2= distance([closestx, closesty], line.coords_end.values)
    if(d1+d2 >= line_len-buffer and d1+d2 <= line_len+buffer):
        ball_to_line = distance(ball.coords.values, [closestx, closesty])
        if ball_to_line <= ball.radius:
            normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty )
            col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
            return True, normal_vector, col_deep
        
    return False, 0, 0

def col_ball_shot(ball, shot):
    '''
    checks for collision of ball and circle
    
    args:
    ball (class: Ball): the ball to check
    circle (class: Circle): the circle to check
    
    returns:
    bool: true if collision is happening, else false
    angle: the angle of the collision (vom Lot aus (TODO: Übersetzen))
    '''
    if distance(ball.coords.values, shot.coords.values) <= ball.radius:
        closestx, closesty = shot.coords_end.x, shot.coords_end.y
        normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty )
        col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
        return True,normal_vector, col_deep
    elif distance(ball.coords.values, shot.coords_end.values) <= ball.radius:
        closestx, closesty = shot.coords_end.x, shot.coords_end.y
        normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty )
        col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
        return True, normal_vector, col_deep
    shot_len = distance(shot.coords.values, shot.coords_end.values)
    dot = ((ball.coords.x-shot.coords.x)* (shot.coords_end.x-shot.coords.x)+ (ball.coords.y-shot.coords.y)* (shot.coords_end.y-shot.coords.y))/shot_len**2
    closestx=shot.coords.x+ (dot*(shot.coords_end.x-shot.coords.x))
    closesty=shot.coords.y+ (dot*(shot.coords_end.y-shot.coords.y))
    buffer = 0.1
    d1= distance([closestx, closesty], shot.coords.values)
    d2= distance([closestx, closesty], shot.coords_end.values)
    if(d1+d2 >= shot_len-buffer and d1+d2 <= shot_len+buffer):
        ball_to_shot = distance(ball.coords.values, [closestx, closesty])
        if ball_to_shot <= ball.radius:
            normal_vector= Vector(ball.coords.x -closestx, ball.coords.y -closesty)
            col_deep = abs(distance([ball.coords.x, ball.coords.y], [closestx, closesty])-ball.radius)
            return True, normal_vector, col_deep
        
    return False, 0, 0


def col_ball_ball(ball, ball2):
    '''
    checks for collision of ball and ball
    
    args:
    ball (class: Ball): the ball to check
    circle (class: Circle): the circle to check
    
    returns:
    bool: true if collision is happening, else false
    angle: the angle of the collision (vom Lot aus (TODO: Übersetzen))
    '''

    collision = False
    if distance(ball.coords.values, ball2.coords.values) <= ball.radius + ball2.radius:
        normal_vector= Vector(ball.coords.x -ball2.coords.x, ball.coords.y -ball2.coords.y)
        normal_vector_norm = Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
        return True, normal_vector_norm
    else:
        return False,Vector(0,0)

    






    

