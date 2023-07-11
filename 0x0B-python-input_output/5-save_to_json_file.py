#!/usr/bin/python3
'''
save to a json file
'''
import json


def save_to_json_file(my_obj, filename):
    '''writes objects to a json file'''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
