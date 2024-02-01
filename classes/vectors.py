# imports
import numpy as np
import math

class Vector:
    '''
    vector from one point to another

    attributes:
    x, y (ints or floats): vector values
    values (numpy.ndarray): vector values as a numpy array
    len (float): length of the vector
    angle (float): angle of the vector starting in positive x-direction

    dunder methods:
    __init__: self explainatory
    __str__: returns attributes of the vector
    __abs__: returns the length of the vector
    __add__: addition of either two vectors or the length of the vector and a number
    __sub__: equivalent to __add__

    other methods:
    rotate: rotates the vector without changing the length
    '''

    def __init__(self, *args):
        '''
        initiation method

        args:
        args (int or float)(2 or 4): if 2 args given the vector will start at (0, 0).
                                    if 4 args given the vector will start at first 2 args and will end at last 2 args
        
        returns: None
        '''
        # x and y
        if len(args) == 2:
            self.x, self.y = args

        elif len(args) == 4:
            self.x = args[2] - args[0]
            self.y = args[3] - args[1]

        self.values = np.array([self.x, self.y])
        
        # length
        self.len = np.sqrt(self.x**2 + self.y**2)

        # angle
        if self.x == 0:
            if self.y > 0:
                self.angle = -np.pi / 2 # negative because y-positive is downwards
            else:
                self.angle = np.pi / 2
        elif self.x > 0:
            self.angle = -np.arctan(self.y / self.x) # negative because y-positive is downwards
        else:
            self.angle = -np.arctan(self.y / self.x) + np.pi # because arctan ranges from -pi/2 to pi/2

        # make angle positive
        if self.angle < 0:
            self.angle += 2 * np.pi


    def __str__(self):
        '''
        returns attributes of the vector
        angle is shown in rad, degree, % of a whole circle

        returns: string
        '''
        return f'\
            Vector with following values:\n\
            x = {self.x}\n\
            y = {self.y}\n\
            length = {abs(self)}\n\
            angle = {self.angle} (rad), {np.degrees(self.angle)} (degree), {np.degrees(self.angle) / 3.6} (% of a whole circle)\n'



    def __abs__(self):
        '''
        should be self explainatory

        returns: length of the vector
        '''

        return self.len
    

    def __add__(self, other):
        '''
        adds two vectors or the length of the vector with a number

        args:
        Vector: adds the two Vectors
        int or float: extends the length of the vector by that number

        returns:
        the resulting length or the resulting Vector

        raises:
        typeError if type is not supported
        '''
        
        if isinstance(other, int) or isinstance(other, float):
            return abs(self) + other
        
        elif isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        
        else:
            raise TypeError(f'cannot add {type(other)} to vector')
        
    
    def __sub__(self, other):
        '''
        subtracts one vector from another or a number from the length of the vector

        args:
        Vector: subtracts another vector from one
        int or float: shortens the length of the vector by that number

        returns:
        the resulting length or the resulting Vector        

        raises:
        typeError if type is not supported
        '''
        
        if isinstance(other, int) or isinstance(other, float):
            return self.len - other
        
        elif isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        
        else:
            raise TypeError(f'cannot subtract {type(other)} from vector')
        


    def rotate(self, angle):
        '''
        rotates the vector without changing its length

        args:
        angle: the angle to rotate the vector (counter clockwise)

        returns: None

        raises:
        TypeError if angle is not int or float
        '''

        if not (isinstance(angle, int) or isinstance(angle, float)):
            raise TypeError(f'angle has to be from type int or float but is {type(angle)}')

        self.angle = (self.angle + angle) % (2 * np.pi)
        self.x = abs(self) * np.cos(self.angle)
        self.y = abs(self) * -np.sin(self.angle)

