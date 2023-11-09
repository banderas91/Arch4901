import math
from shape import Shape2D

class Circle(Shape2D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius
