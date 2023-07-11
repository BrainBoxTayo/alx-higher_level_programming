#!/usr/bin/python3
'''
module to define a class student
'''


class Student:
    ''' The class Student '''

    def __init__(self, first_name, last_name, age):
        '''Initialization Module'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''same as 8-class_to_json'''
        dicts = {}
        if type(attrs) == list:
            for j in attrs:
                if hasattr(self, j):
                    dicts[j] = getattr(self, j)
                else:
                    continue
            return (dicts)
        else:
            return (vars(self))

    def reload_from_json(self, json):
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
