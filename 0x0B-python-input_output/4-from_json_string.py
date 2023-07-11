#!/usr/bin/python3
'''
module that returns an object represented by a JSON string
'''
import json


def from_json_string(my_str):
    '''function that performs what is said above'''
    return (json.loads(my_str))
