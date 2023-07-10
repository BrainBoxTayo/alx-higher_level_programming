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
