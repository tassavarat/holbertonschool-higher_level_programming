The ``2-matrix_divided`` module
===============================

Using ``matrix_divided``
------------------------

	>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Integer division:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, 3)
	[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

Non int or float:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, "holberton", 6]
	... ]
	>>> matrix_divided(matrix, 3)
	Traceback (most recent call last):	
	TypeError: matrix must be a matrix (list of lists) of integers/floats

Different size:
	>>> matrix = [
	...	[1, 2],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, 3)
	Traceback (most recent call last):	
	TypeError: Each row of the matrix must have the same size

Divide by string:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, "school")
	Traceback (most recent call last):	
	TypeError: div must be a number

Divide by zero:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, 0)
	Traceback (most recent call last):	
	ZeroDivisionError: division by zero

Empty matrix:
	>>> matrix = [
	...	[],
	...	[]
	... ]
	>>> matrix_divided(matrix, 3)
	Traceback (most recent call last):	
	TypeError: matrix must be a matrix (list of lists) of integers/floats

None as matrix:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(None, 3)
	Traceback (most recent call last):	
	TypeError: matrix must be a matrix (list of lists) of integers/floats

None as div:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, None)
	Traceback (most recent call last):	
	TypeError: div must be a number

No matrix passed:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(, 3)
	Traceback (most recent call last):	
	SyntaxError: invalid syntax

No div passed:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, None)
	Traceback (most recent call last):	
	TypeError: div must be a number

Inf as div passed:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, float("inf"))
    	[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

NaN as div passed:
	>>> matrix = [
	...	[1, 2, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, float("nan"))
	Traceback (most recent call last):	
	TypeError: div must be a number

Mixed types:
	>>> matrix = [
	...	[1, 2.5, 3],
	...	[4, 5, 6]
	... ]
	>>> matrix_divided(matrix, 3)
    	[[0.33, 0.83, 1.0], [1.33, 1.67, 2.0]]
