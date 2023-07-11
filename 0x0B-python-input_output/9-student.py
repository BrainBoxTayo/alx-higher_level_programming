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

    def to_json(self):
        '''same as 8-class_to_json'''
        return (vars(self))
