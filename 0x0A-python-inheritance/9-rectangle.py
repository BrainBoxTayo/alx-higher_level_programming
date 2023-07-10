#!/usr/bin/python3
"""The rectangle subclass of the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class for rectangles"""

    def __init__(self, width, height):
        """initializes a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area implementation"""
        return self.__width * self.__height

    def __repr__(self):
        """repr to return a string on print"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
