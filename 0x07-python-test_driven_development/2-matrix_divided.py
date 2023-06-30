#!/usr/bin/python3
'''
divide all elements of a matrix module
'''


def matrix_divided(matrix,div):
    '''
    function to do the task given above
    '''
    matrix = [["billy"], [90,23]]
    if not all(isinstance([[number for number in group] for group in matrix], (int, float))):
        print("Yo")
