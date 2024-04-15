#!/usr/bin/env python3

class Shape:
    "Super class for various geometrical shapes."
    def area(self):
        "Calculate the area of the shape."
        raise NotImplementedError("This method should be overridden by subclasses")

    def perimeter(self):
        "Calculate the perimeter of the shape."
        raise NotImplementedError("This method should be overridden by subclasses")
