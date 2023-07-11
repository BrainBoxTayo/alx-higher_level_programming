#!/usr/bin/python3
'''
Module foe Tech Interview Prep
'''


def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    if n > 2:
        lists = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(lists[i - 1][j - 1] + lists[i - 1][j])
            row.append(1)
            lists.append(row)
        return lists
