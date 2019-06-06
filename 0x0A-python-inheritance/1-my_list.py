#!/usr/bin/python3
class MyList(list):
    """Inherits from list
    """
    def print_sorted(self):
        """Prints the list in ascending order
        """
        print(sorted(self))
