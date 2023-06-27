#!/usr/bin/python3
"""Class of type square with size attribute"""


class Square:

    """Representing a square"""
    def __init__(self, size=0):

        """initializer for class square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """Area for the square"""
        return (self.__size * self.__size)
