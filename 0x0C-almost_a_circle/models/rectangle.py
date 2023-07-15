#!/usr/bin/python3
'''
Rectangle Class
'''
from models.base import Base


class Rectangle(Base):
    '''
    The rectangle class defines a rectangle
        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        Methods:
            Getters and setters for width and height
            __type__checker: checks if the input is an integer
            __zero_checker: checks if the input is greater than 0
            area: returns the area of the rectangle
            display: print visual representation of the rectangle
            update: assigns an argument to each attribute (updates an instance)
    '''

    def __init__(self, width, height,  x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        names = list(vars(self))
        i = 0
        if args and len(args) > 0:
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
            return
        else:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__type_checker(width, "width")
        self.__zero_checker(width, "width")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__type_checker(height, "height")
        self.__zero_checker(height, 'height')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__type_checker(x, 'x')
        self.__zero_checker(x, 'x')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__type_checker(y, 'y')
        self.__zero_checker(y, 'y')
        self.__y = y

    def area(self):
        return (self.width * self.height)

    def display(self):
        for space_y in range(self.y):
            print()
        for i in range(self.height):
            for space_x in range(self.x):
                print(' ', end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __type_checker(self, input, string):
        if type(input) is not int:
            raise TypeError("{} must be an integer".format(string))

    def __zero_checker(self, input, string):
        if input <= 0 and (string == "width" or string == "height"):
            raise ValueError("{} must be > 0".format(string))
        if input < 0 and (string == 'x' or string == 'y'):
            raise ValueError("{} must be >= 0".format(string))

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
