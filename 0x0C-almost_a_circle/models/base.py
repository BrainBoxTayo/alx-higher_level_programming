#!/usr/bin/python3
'''
Base Class for the project
'''
import json


class Base:
    '''
    Base Class for 
    Attributes:
        id (int): id of the object
    Methods:
        __init__(self, id=None): initializes the id
        to_json_string(list_dictionaries): returns the JSON string representation of list_dictionaries
        save_to_file(cls, list_objs): writes the JSON string representation to a file
    '''    
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return (json.dumps(list_dictionaries))

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
