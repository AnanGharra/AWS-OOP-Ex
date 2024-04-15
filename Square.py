#!/usr/bin/env python3

from Shape import Shape

class Square(Shape):
    "A class representing a square."

    def __init__(self, side_length):
        "Initialize the square with a side length."
        self.side_length = side_length

    def get_side_length(self):
        "Return the side length of the square."
        return self.side_length

    def set_side_length(self, length):
        "Set the side length of the square."
        self.side_length = length

    def area(self):
        "Calculate and return the area of the square."
        return self.side_length ** 2

    def perimeter(self):
        "Calculate and return the perimeter of the square."
        return 4 * self.side_length
