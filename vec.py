from typing import Union
from math import pi, sqrt

def deg_to_rad(angle: float) -> float:
    return angle * pi / 180

def rad_to_deg(angle: float) -> float:
    return angle * 180 / pi

def get_vector(start: 'vec2', end: 'vec2'):
    return vec2((end.x - start.x, start.y - end.y))

def shortest_angle_diff(a, b):
    # Function to calculate the shortest angle difference
    return ((a - b + 180) % 360) - 180

def lerp(a, b, t):
    return a + (b - a) * t

class vec2:
    def __init__(self, arg: Union[tuple, list, 'vec2']):
        if isinstance(arg, tuple) or isinstance(arg, list):
            self.x, self.y = arg[0], arg[1]
        elif isinstance(arg, vec2):
            self.x, self.y = arg.x, arg.y
        else:
            raise ValueError("Invalid arguments for vec2 initialization")

    def __mul__(self, val):
        if isinstance(val, int) or isinstance(val, float):
            return vec2((self.x * val, self.y * val))
        else:
            raise ValueError("Invalid arguments for vec2 multiplication. Only float and int allowed.")

    def __add__(self, val):
        if isinstance(val, vec2):
            return vec2((self.x + val.x, self.y + val.y))
        elif isinstance(val, int) or isinstance(val, float):
            return vec2((self.x + val, self.y + val))
        else:
            raise ValueError("Invalid arguments for vec2 addition. Only vec2, float and int allowed.")
    
    def __sub__(self, val):
        if isinstance(val, vec2):
            return vec2((self.x - val.x, self.y - val.y))
        elif isinstance(val, int) or isinstance(val, float):
            return vec2((self.x - val, self.y - val))
        else:
            raise ValueError("Invalid arguments for vec2 subtraction. Only vec2, float and int allowed.")
        
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            magnitude = 1e-9
        self.norm_x = float(self.x / magnitude)
        self.norm_y = float(self.y / magnitude)
        return vec2((self.norm_x, self.norm_y))
    
    def __call__(self):
        return (self.x, self.y)
    
    def __iter__(self):
        return iter((self.x, self.y))

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __repr__(self):
        return f"({self.x}, {self.y})"
    

class vec3:
    def __init__(self, arg: Union[tuple, list, 'vec3']):
        if isinstance(arg, tuple) or isinstance(arg, list):
            self.x, self.y, self.z = arg[0], arg[1], arg[2]
        elif isinstance(arg, 'vec3'):
            self.x, self.y, self.z = arg.x, arg.y, arg.z
        else:
            raise ValueError("Invalid arguments for vec3 initialization. arg must be [tuple, list, vec3]")

    def __mul__(self, val):
        if isinstance(val, int) or isinstance(val, float):
            return vec3((self.x * val, self.y * val, self.z * val))
        else:
            raise ValueError("Invalid arguments for vec3 multiplication. Only float and int allowed.")

    def __add__(self, val):
        if isinstance(val, vec3):
            return vec3((self.x + val.x, self.y + val.y, self.z + val.z))
        elif isinstance(val, int) or isinstance(val, float):
            return vec3((self.x + val, self.y + val, self.z + val))
        else:
            raise ValueError("Invalid arguments for vec2 addition. Only vec2, float and int allowed.")
    
    def __sub__(self, val):
        if isinstance(val, vec2):
            return vec3((self.x - val.x, self.y - val.y, self.z - val.z))
        elif isinstance(val, int) or isinstance(val, float):
            return vec3((self.x - val, self.y - val, self.z - val))
        else:
            raise ValueError("Invalid arguments for vec2 subtraction. Only vec2, float and int allowed.")

    def normalized(self):
        magnitude = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2) 
        if magnitude == 0:
            magnitude = 1e-9
        self.norm_x = float(self.x / magnitude)
        self.norm_y = float(self.y / magnitude)
        self.norm_z = float(self.y / magnitude)
        return vec3((self.norm_x, self.norm_y, self.norm_z))
    
    def __call__(self):
        return (self.x, self.y, self.z)
    
    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range")

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"