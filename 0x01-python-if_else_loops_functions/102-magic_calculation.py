#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    else:
        if c > b:
            return (b + a)
        else:
            b = b * a
            c = c - b
            return c
