#!/usr/bin/python3
'''
divide all elements of a matrix module
'''


def matrix_divided(matrix, div):
    '''
     Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    '''
    typeError1 = "matrix must be a matrix (list of lists) of integers/floats"
    new_mat = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix)
    if (length < 2):
        # handles if the list of list passed is only a single list
        #  in another list
        raise TypeError(typeError1)
    for i in range(0, length):
        # this checks if all the lists are equal in size
        if not isinstance(matrix[i], list):
            raise TypeError(typeError1)
        if i + 1 == length:
            break
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(0, len(matrix)):
        # this is where the division happens
        inner_list = []
        for j in range(0, len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(typeError1)
            inner_list.append(round((matrix[i][j] / div), 2))
        new_mat.append(inner_list)
    return new_mat
