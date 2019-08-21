#!/usr/bin/python3
"""6-peak module"""


def find_peak(list_of_integers):
    """Finds a peak
    list_of_integers - Given values
    Return: Peak
    """
    length = len(list_of_integers)
    i = length//2
    # if i != 0:
    # print("list_of_integers is", list_of_integers)
    # print("list_of_integers[{}] is {}".format(i, list_of_integers[i]))

    if i == 0:
        return None
    elif list_of_integers[i] < list_of_integers[i - 1]:
        while list_of_integers[i - 1] > list_of_integers[i]:
            # print("left i is", list_of_integers[i])
            i = i - 1
    elif list_of_integers[i] < list_of_integers[i + 1]:
        while i < length - 1 and list_of_integers[i + 1] > list_of_integers[i]:
            # print("right i is", list_of_integers[i])
            i = i + 1
    return list_of_integers[i]
