# imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import numpy as np
import pygame
import math

import functions.collisions as coll
import vars.const as const
import vars.setup as setup
import functions.sound as sound
import functions.general as general
from vars.setup import ball_group, wall_group, circle_group, flipper_group, line_group, shot_group
from classes.vectors import Vector



# definition of the
#  class
class Ball(pygame.sprite.Sprite):
    '''
    Balls, theres nothing more to say, its just the class for the Balls in the game
    subclass of pygame.sprite.Sprite to make it compatible with pygame groups
    
    class attributes:
    gravity: acceleration of the ball in y+ direction (downwards)

    object attributes:
    coords (Vector)(2-dimensional): coordinates of the Ball center
    radius (int or float): size of the ball
    speed (Vector)(2-dimensional): speed of the Ball
    index (int): some index number to log the order of the walls (idk if this will be usefull sometime)
                                                this will only exist if arg group == True

    dunder methods:
    __init__: initiation method of the class
    __str__: attributes of the ball

    other methods:
    update: does all the logical and graphical updates of the ball
    rotate: returns a copy of the ball with rotated coordinates by a given angle
    '''

    # global gravity to all balls (maybe this will become a object specific attribute later)
    gravity = const.gravity
    # gravity = Vector(0, 0)

    def __init__(self, x, y, radius = setup.ball_rad, speed = None, group = True):
        '''
        initiation of a ball object

        args:
        x, y: initial coordinates of the ball
        radius: (initial) radius of the ball
        speed: initial speed of the ball
        group: determines if the ball is added to ball_group and gets an index

        raises:
        Type Error if argument speed is a not supported type
        '''

        super().__init__()

        self.coords = Vector(x, y)
        self.radius = radius
        self.reibung = 0.93
        self.energy = 1.03
        self.ball_coll=False

        if speed is None:
            self.speed = Vector(0, 0)
        elif isinstance(speed, tuple) or isinstance(speed, list) or isinstance(speed, np.ndarray):
            self.speed = Vector(speed[0], speed[1])
        elif isinstance(speed, Vector):
            self.speed = speed
        else:
            raise TypeError(f'type not supported (yet). Already supported types for argument "speed" are NoneType, tuple, list, numpy.ndarray and Vector. Given argument is from type {type(speed)}')

        if group:
            self.index = max([0]+[ball.index for ball in ball_group]) + 1
            ball_group.add(self)
            

        self.test = True

    def __str__(self):
        '''
        returns attributes of the ball
        '''
        return f'\
            Ball with positional vector:\n{self.coords}\n\n\
            velocity:\n{self.speed}\n\n\
            gravity:\n{self.gravity}\n\n\
            radius: {self.radius}\n'


    def draw(self):
        pygame.draw.circle(setup.screen, 'black', self.coords.values, self.radius, width = 2)
        pygame.draw.circle(setup.screen, 'white', self.coords.values, self.radius - 2)
        pygame.draw.circle(setup.screen, 'blue', self.coords.values, self.radius - 18)
        pygame.draw.circle(setup.screen, 'black', self.coords.values, 4)


    def move(self):
        '''
        move the ball and update its velocity
        checks for collisions before (TODO)

        returns: None
        '''
        self.speed += self.gravity
        self.coords += self.speed


    def update(self):
        '''
        does all the logical and graphical updates for the ball:
        
        movement updates
        drawing

        
        returns: None
        '''
        
        self.move()
        self.ball_coll=False
        for circle in circle_group:
            is_colliding, normal_vector = coll.col_ball_circle(self, circle)
            if is_colliding and self.test:
                    #self.coords -= self.speed
                    col_deep = abs(general.distance([self.coords.x, self.coords.y], [circle.coords.x, circle.coords.y])-(self.radius+circle.radius))
                    normal_vector_norm =  Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
                    dot_product = self.speed.x * normal_vector.x + self.speed.y * normal_vector.y
                    magnitude_normal = math.sqrt(normal_vector.x ** 2 + normal_vector.y ** 2)
                    parallel_scalar = dot_product / (magnitude_normal ** 2)
                    parallel_vector = (normal_vector.x * parallel_scalar, normal_vector.y * parallel_scalar)
                    perpendicular_vector = (self.speed.x - parallel_vector[0], self.speed.y - parallel_vector[1])
                    # Resultierende Geschwindigkeiten
                    # Resultierenden Vektor berechnen
                    self.coords += Vector(normal_vector_norm.x*col_deep, normal_vector_norm.y*col_deep)
                    self.speed.x = (-parallel_vector[0] + perpendicular_vector[0])*self.energy
                    self.speed.y = (-parallel_vector[1] + perpendicular_vector[1])*self.energy
                    self.ball_coll = True
                    

        for flipper in flipper_group:
            is_colliding, normal_vector, v_vector, col_deep = coll.col_ball_flipper(self, flipper)
            if is_colliding and self.test:

                    normal_vector_norm =  Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
                    dot_product = self.speed.x * normal_vector.x + self.speed.y * normal_vector.y
                    magnitude_normal = math.sqrt(normal_vector.x ** 2 + normal_vector.y ** 2)
                    parallel_scalar = dot_product / (magnitude_normal ** 2)
                    parallel_vector = (normal_vector.x * parallel_scalar, normal_vector.y * parallel_scalar)
                    perpendicular_vector = (self.speed.x - parallel_vector[0], self.speed.y - parallel_vector[1])
                    ##Es muss noch die Geschwindigkeit des Kollisionspunktes auf dem Kreis addiert werden 
                    # Resultierenden Vektor berechnen
                    if flipper.check_velocity:
                        #self.coords -= self.speed
                        self.coords += Vector(normal_vector_norm.x*col_deep, normal_vector_norm.y*col_deep)
                        self.coords += v_vector+ v_vector
                        self.speed.x = (-parallel_vector[0] + perpendicular_vector[0]+ v_vector.x)*self.reibung
                        self.speed.y = (-parallel_vector[1] + perpendicular_vector[1]+ v_vector.y)*self.reibung
                    else:
                        #self.coords -= self.speed
                        self.coords += Vector(normal_vector_norm.x*col_deep, normal_vector_norm.y*col_deep)
                        self.speed.x = (-parallel_vector[0] + perpendicular_vector[0])*self.reibung
                        self.speed.y = (-parallel_vector[1] + perpendicular_vector[1])*self.reibung

                        
        
        for line in line_group:
            is_colliding, normal_vector, col_deep = coll.col_ball_line(self, line)
            if is_colliding and self.test:
                    #self.coords -= self.speed
                    #self.speed.rotate(2*-(coll_angle - self.speed.angle))
                    normal_vector_norm =  Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
                    dot_product = self.speed.x * normal_vector.x + self.speed.y * normal_vector.y
                    magnitude_normal = math.sqrt(normal_vector.x ** 2 + normal_vector.y ** 2)
                    parallel_scalar = dot_product / (magnitude_normal ** 2)
                    parallel_vector = (normal_vector.x * parallel_scalar, normal_vector.y * parallel_scalar)
                    perpendicular_vector = (self.speed.x - parallel_vector[0], self.speed.y - parallel_vector[1])

                    # Resultierenden Vektor berechnen
                    self.coords += Vector(normal_vector_norm.x*col_deep, normal_vector_norm.y*col_deep)
                    self.speed.x = (-parallel_vector[0] + perpendicular_vector[0])*self.reibung
                    self.speed.y = (-parallel_vector[1] + perpendicular_vector[1])*self.reibung
                    #self.coords += self.speed

        for shot in shot_group:
            is_colliding, normal_vector, col_deep = coll.col_ball_shot(self, shot)
            if is_colliding and self.test:
                    #self.speed.rotate(2*-(coll_angle - self.speed.angle))
                    normal_vector_norm =  Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
                    dot_product = self.speed.x * normal_vector.x + self.speed.y * normal_vector.y
                    magnitude_normal = math.sqrt(normal_vector.x ** 2 + normal_vector.y ** 2)
                    parallel_scalar = dot_product / (magnitude_normal ** 2)
                    parallel_vector = (normal_vector.x * parallel_scalar, normal_vector.y * parallel_scalar)
                    perpendicular_vector = (self.speed.x - parallel_vector[0], self.speed.y - parallel_vector[1])

                    # Resultierenden Vektor berechnen
                    if shot.check_velocity:
                        #self.coords -= self.speed
                        self.coords += Vector(normal_vector_norm.x*col_deep, normal_vector_norm.y*col_deep)
                        self.coords += Vector(shot.nv.x *shot.speed, shot.nv.y *shot.speed)
                        self.speed.x = (-parallel_vector[0] + perpendicular_vector[0]+ shot.nv.x *shot.speed)*self.reibung
                        self.speed.y = (-parallel_vector[1] + perpendicular_vector[1]+ shot.nv.y *shot.speed)*self.reibung
                    else:
                        #self.coords -= self.speed
                        self.coords += Vector(normal_vector_norm.x*col_deep, normal_vector_norm.y*col_deep)
                        #self.coords += Vector(shot.nv.x *shot.speed, shot.nv.y *shot.speed)
                        self.speed.x = (-parallel_vector[0] + perpendicular_vector[0])*self.reibung
                        self.speed.y = (-parallel_vector[1] + perpendicular_vector[1])*self.reibung
                         


        for ball in ball_group:
            if self.index != ball.index:
                is_colliding, normal_vector = coll.col_ball_ball(self, ball)
                if is_colliding and self.test:
                        #self.coords -= self.speed
                        col_deep = abs(general.distance([self.coords.x, self.coords.y], [ball.coords.x, ball.coords.y])-(self.radius+ball.radius))
                        normal_vector_norm =  Vector(normal_vector.x/normal_vector.__abs__(), normal_vector.y/normal_vector.__abs__())
                        # Geschwindigkeiten umrechnen
                        
                        dot_product1 = self.speed.x * normal_vector.x + self.speed.y * normal_vector.y
                        dot_product2 = ball.speed.x * normal_vector.x + ball.speed.y * normal_vector.y

                        # Impuls und Energieerhaltung
                        total_mass = 2  # Masse beider Bälle (vereinfacht auf gleiche Masse)
                        new_speed1 = [(2 * dot_product2 * normal_vector.x - self.speed.x) / total_mass,
                                    (2 * dot_product2 * normal_vector.y - self.speed.y) / total_mass]
                        new_speed2 = [(2 * dot_product1 * normal_vector.x - ball.speed.x) / total_mass,
                                    (2 * dot_product1 * normal_vector.y - ball.speed.y) / total_mass]

                        # Resultierende Vektoren
                        self.coords += Vector(normal_vector_norm.x*col_deep, normal_vector_norm.y*col_deep)
                        ball.coords -= Vector(normal_vector_norm.x*col_deep, normal_vector_norm.y*col_deep)
                        self.speed = Vector(new_speed1[0]*self.reibung, new_speed1[1]*self.reibung)
                        ball.speed = Vector(new_speed2[0]*self.reibung, new_speed2[1]*self.reibung)
                        
                        
                        
            
        self.draw()

        # TODO:
        # movement updates (to be updated (no thats not intended))
        # collision checks


    def rotate(self, angle):
        '''
        rotate the coordinates of a ball by a given angle

        args:
        ball (class: Ball): The ball of which the coordinates will be rotated
        angle (in rad): The angle to rotate the coordinates

        returns:
        a new instance of class Ball
        '''

        old_coords = self.coords.values # coordinates as numpy array (see: classes.vectors)
        old_speed = self.speed.values
        rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) # rotation matrix (clockwise due to the positive y direction being downwards)
        new_coords = np.dot(old_coords, rotation).tolist()
        new_speed = np.dot(old_speed, rotation).tolist()

        return Ball(*new_coords, self.radius, speed = new_speed, group = False)



