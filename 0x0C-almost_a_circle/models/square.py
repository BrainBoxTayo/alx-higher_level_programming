#!/usr/bin/python3
'''
class Square
'''
from models.rectangle import Rectangle


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
        if args and len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}