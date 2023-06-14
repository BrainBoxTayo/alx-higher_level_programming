#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = matrix.copy()
    '''compute the square value of all integers in a matrix'''
    for i in range(len(matrix)):
        new_mat[i] = list(map(lambda x: x ** 2, new_mat[i]))
    return new_mat
