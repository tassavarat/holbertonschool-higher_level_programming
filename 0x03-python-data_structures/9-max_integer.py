#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        large = my_list[0]
        for i in my_list[1:]:
            if large < i:
                large = i
        return large
    return None
