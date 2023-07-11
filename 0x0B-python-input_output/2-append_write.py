#!/usr/bin/python3
'''
module to append strings
'''


def append_write(filename="", text=""):
    """function that writes text to filename"""
    with open(filename, 'a', encoding="utf-8") as f:
        no_char = f.write(text)
    return no_char
