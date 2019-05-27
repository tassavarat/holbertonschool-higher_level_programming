The ``4-print_square`` module
=============================

Using ``print_square``
----------------------

	>>> print_square = __import__('4-print_square').print_square

4x4 square:
	>>> print_square(4)
	####
	####
	####
	####

0:
	>>> print_square(0)
	
-1:
	>>> print_square(-1)
    	Traceback (most recent call last):
    	ValueError: size must be >= 0
	
String:
	>>> print_square("string")
    	Traceback (most recent call last):
    	TypeError: size must be an integer

Infinity:
	>>> print_square(float("inf"))
    	Traceback (most recent call last):
    	TypeError: size must be an integer

NaN:
	>>> print_square(float("nan"))
    	Traceback (most recent call last):
    	TypeError: size must be an integer

No argument
	>>> print_square()
    	Traceback (most recent call last):
    	TypeError: print_square() missing 1 required positional argument: 'size'
