#!/usr/bin/python3
"""6-peak module"""


def find_peak(list_of_integers):
    """Finds a peak
    list_of_integers - Given values
    Return: Peak
    """
    i = len(list_of_integers)//2

    if i == 0:
        return None
    elif list_of_integers[i] < list_of_integers[i - 1]:
        while list_of_integers[i - 1] > list_of_integers[i]:
            i = i - 1
    elif list_of_integers[i] < list_of_integers[i + 1]:
        while list_of_integers[i + 1] > list_of_integers[i]:
            i = i + 1
    return list_of_integers[i]
