#!/usr/bin/python3
'''
Base Class for the project
'''
import json
import csv
import turtle


class Base:
    '''
    Base Class for
    Attributes:
        id (int): id of the object
    Methods:
        __init__(self, id=None): initializes the id
        to_json_string(list_dictionaries): returns the JSON representation
        save_to_file(cls, list_objs): writes the JSON representation to a
                                    file
        from_json_string(json_string): returns the objects of the JSON string
        create(cls, **dictionary): returns an instance with all
                                    attributes already set
        load_from_file(cls): returns a list of instances
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.penup()
        for shape in list_rectangles:
            turtle.setpos(shape.x, shape.y)
            turtle.pendown()
            turtle.fd(shape.width)
            turtle.lt(90.0)
            turtle.back(shape.height)
            turtle.rt(90.0)
            turtle.back(shape.width)
            turtle.lt(90.0)
            turtle.fd(shape.height)
            turtle.penup()
        for shape in list_squares:
            turtle.setpos(shape.x, shape.y)
            turtle.pendown()
            turtle.fd(shape.width)
            turtle.lt(90.0)
            turtle.back(shape.height)
            turtle.rt(90.0)
            turtle.back(shape.width)
            turtle.lt(90.0)
            turtle.fd(shape.height)
            turtle.penup()
        turtle.done()
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                else:
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                else:
                    fields = ['id', 'size', 'x', 'y']
                list_dicts = csv.DictReader(f, fieldnames=fields)
                list_dicts = [dict([i, int(j)] for i, j in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        from rectangle import Rectangle
        from square import Square

        __rect_string = ""
        __square_string = ""
        list_of_dicts_rect = []
        list_of_dicts_square = []
        for obj in list_objs:
            if isinstance(obj, Rectangle) and type(obj) is Rectangle:
                list_of_dicts_rect.append(obj.to_dictionary())
            elif isinstance(obj, Square) and type(obj) is Square:
                list_of_dicts_square.append(obj.to_dictionary())
        __rect_string += cls.to_json_string(list_of_dicts_rect)
        __square_string += cls.to_json_string(list_of_dicts_square)
        with open("Rectangle.json", 'w') as f:
            f.write(__rect_string)
        with open("Square.json", 'w') as f:
            f.write(__square_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            with open("{}.json".format(cls.__name__)) as f:
                list_of_instance = []
                list_of_dicts = cls.from_json_string(f.read())
                for dicts in list_of_dicts:
                    new_instance = cls.create(**dicts)
                    list_of_instance.append(new_instance)
                return list_of_instance
        except FileNotFoundError:
            return ([])
    
