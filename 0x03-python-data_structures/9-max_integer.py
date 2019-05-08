#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        large = 0
        for i in my_list:
            if large <= i:
                large = i
        return large
    return None
