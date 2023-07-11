#!/usr/bin/python3
'''
creates an Object from a “JSON file”
'''
import json


def load_from_json_file(filename):
    '''loads obkects from a json file'''
    with open(filename, 'r') as f:
        string = f.read()
        return json.loads(string)
