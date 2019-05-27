The ``3-say_my_name`` module
============================

Using ``say_my_name``
---------------------

	>>> say_my_name = __import__('3-say_my_name').say_my_name

Regular functionality:
	>>> say_my_name("John", "Smith")
	My name is John Smith

First name:
	>>> say_my_name("Bob")
	My name is Bob 

Last name:
	>>> say_my_name(, "Smith")
    	Traceback (most recent call last):
	SyntaxError: invalid syntax

Int as first name:
	>>> say_my_name(12, "White")
    	Traceback (most recent call last):
	TypeError: first_name must be a string

Int as first name:
	>>> say_my_name("John", 12)
    	Traceback (most recent call last):
	TypeError: last_name must be a string

None as first name:
	>>> say_my_name(None, "Smith")
    	Traceback (most recent call last):
	TypeError: first_name must be a string

None as last name:
	>>> say_my_name("John", None)
    	Traceback (most recent call last):
	TypeError: last_name must be a string

Empty string:
	>>> say_my_name("", "")
	My name is  

No arguments:
	>>> say_my_name()
    	Traceback (most recent call last):
	TypeError: say_my_name() missing 1 required positional argument: 'first_name'
