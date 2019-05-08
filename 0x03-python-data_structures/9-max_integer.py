#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        large = 0
        for i in my_list:
            if i >= large:
                large = i
        return large
    return None
