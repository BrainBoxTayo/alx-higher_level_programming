#!/usr/bin/python3
'''
module for reading and printing a file
'''


def read_file(filename=""):
    '''function that does the task'''
    with open(filename) as f:
        print(f.read())
