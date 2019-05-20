#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            tmp = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            tmp = 0
        except ZeroDivisionError:
            print("division by 0")
            tmp = 0
        except IndexError:
            print("out or range")
            tmp = 0
        finally:
            result.append(tmp)
    return result
