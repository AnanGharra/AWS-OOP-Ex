#!/usr/bin/env python3

from Shape impoer Shape
import math

class Circle(Shape):
    "A class representing a circle."
    
    def __init__(self, radius):
        "Initialize the circle with a radius."
        self.radius = radius

    def get_radius(self):
        "Return the radius of the circle."
        return self.radius

    def set_radius(self, radius):
        "Set the radius of the circle."
        self.radius = radius

    def area(self):
        "Calculate and return the area of the circle."
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        "Calculate and return the perimeter of the circle."
        return 2 * math.pi * self.radius
