#!/usr/bin/python3
'''
class Square
'''
from __future__ import annotations
from rectangle import Rectangle


class Square(Rectangle):
    '''
    The Square class defines a Square, but it inherits from Rectangle
    Attributes:
        size (int): size of the square
        x (int): x coordinate of the square
        y (int): y coordinate of the square
        id (int): id of the square
    Methods:
        __init__(self, size, x=0, y=0, id=None)
        __str__(self)
        update(self, *args, **kwargs)
        to_dictionary(self): returns the dictionary representation of a Square
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
        self.__size = size

    def update(self, *args, **kwargs):
        names = list(vars(self))
        i = 0
        if args and len(args) > 0:
            for arg in args:
                setattr(self, names[i], arg)
                if i == 1:
                    i += 1
                if i == 4:
                    return
                i += 1
            return
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
