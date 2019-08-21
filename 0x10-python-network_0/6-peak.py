#!/usr/bin/python3
"""6-peak module"""


def find_peak(list_of_integers):
    """Finds a peak
    list_of_integers - Given values
    Return: Peak
    """

    length = len(list_of_integers)
    mid = length
    i = length // 2

    if i == 0:
        return None

    while True:
        mid = mid // 2
        if i > 0 and list_of_integers[i] < list_of_integers[i - 1]:
            if mid // 2 == 0:
                mid = 2
            i = i - mid//2
        elif i + 1 < length and list_of_integers[i] < list_of_integers[i + 1]:
            if mid // 2 == 0:
                mid = 2
            i = i + mid//2
        else:
            return list_of_integers[i]
