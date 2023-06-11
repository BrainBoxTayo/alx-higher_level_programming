#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = 0
    for i in matrix:
        for j in i:
            if j == matrix[a][-1]:
                print("{:d}".format(j), end="")
                a += 1
                continue
            print("{:d} ".format(j), end="")
        print()
