#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{:1d}".format(matrix[i][j]), end="")
                continue
            print("{:1d} ".format(matrix[i][j]), end="")
        print("\n",end="")
