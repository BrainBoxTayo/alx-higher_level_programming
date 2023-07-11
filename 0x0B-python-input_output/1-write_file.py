#!/usr/bin/python3
'''
module to write strings
'''


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        no_char = f.write(text)
    return no_char
