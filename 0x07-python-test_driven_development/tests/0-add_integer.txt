The ``0-add_integer'' module
============================

Using ``add_integer``
---------------------

	>>> add_integer = __import__('0-add_integer').add_integer

Regular integers:
	>>> add_integer(1, 2)
	3

Negative number:
	>>> add_integer(100, -2)
	98

Single argument:
	>>> add_integer(2)
	100

Float:
	>>> add_integer(100.3, -2)
	98

Passing string to b:
	>>> add_integer(4, "School")
	Traceback (most recent call last):
	TypeError: b must be an integer

Passing string to a:
	>>> add_integer(None)
	Traceback (most recent call last):
	TypeError: a must be an integer

Name error:
	>>> add_integer(1, h)
	Traceback (most recent call last):
	NameError: name 'h' is not defined

No parameters:
	>>> add_integer()
	Traceback (most recent call last):
	TypeError: add_integer() missing 1 required positional argument: 'a'

Adding infinity:
	>>> add_integer(1, float("inf"))
	Traceback (most recent call last):
    	OverflowError: cannot convert float infinity to integer

Adding NaN:
	>>> add_integer(1, float("nan"))
	Traceback (most recent call last):
    	ValueError: cannot convert float NaN to integer
