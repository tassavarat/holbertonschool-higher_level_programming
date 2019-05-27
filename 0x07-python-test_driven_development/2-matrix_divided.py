#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    """
    if matrix:
        for i in matrix:
            if any(type(j) is not int and type(j) is not float for j in i)\
                    or type(matrix) is not list or len(i) == 0:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        matrix_len = len(matrix[0])
        for i in matrix:
            if matrix_len != len(i):
                raise TypeError("Each row of the matrix must have the same\
 size")
    else:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(div) is not int and type(div) is not float or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(j / div, 2) for j in i]for i in matrix]
