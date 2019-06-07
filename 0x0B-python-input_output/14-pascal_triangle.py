#!/usr/bin/python3
"""14-pascal_triangle module
"""


def factorial(n):
    """Returns factorialorial
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle
    of n
    """
    res = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        res.append(row)
    return res
