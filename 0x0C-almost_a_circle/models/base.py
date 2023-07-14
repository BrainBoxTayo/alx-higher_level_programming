#!/usr/bin/python3
'''
Base Class for the project
'''

class Base:
    '''Goal is to manage the id attribute'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        