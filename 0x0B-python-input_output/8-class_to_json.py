#!/usr/bin/python3
'''
module that returns the dictionary description with simple data
'''


def class_to_json(obj):
    members = vars(obj)
    return (members)
