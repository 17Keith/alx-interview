#!/usr/bin/python3
"""A funtion that returns a list of lists of integers\
    representing the Pascal's triangle of 'n'"""


def pascal_triangle(n):
    """Function that prints a list of integers representing the pascal triangle"""
    row = []
    if n == 0:
        return row
    for i in range(n):
        row.append([])
        row[i].append(1)

        if (i > 0):
            for j in range(1, i):
                row[i].append(row[i - 1][j - 1] + row[i - 1][j])
            row[i].append(1)
    return row
