#!/usr/bin/python3
"""
function pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):

    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    """

    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        row = [1]
        last_row = triangle[-1]

        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i + 1])

        row.append(1)
        triangle.append(row)

    return triangle
