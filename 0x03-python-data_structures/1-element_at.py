#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= 0 and idx < len(my_list):
        for i in range(len(my_list)):
            if i is idx:
                return my_list[i]
    return None
