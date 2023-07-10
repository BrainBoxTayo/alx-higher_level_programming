#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """The base geometry class"""

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator funcrion"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class for rectangles"""
    def __init__(self, width, height):
        """initializes a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
