#!/usr/bin/python3
def max_integer(my_list=[]):
    """Return the biggest integer of a list."""
    if len(my_list) == 0:
        return None

    maxnum = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxnum:
            maxnum = my_list[i]
    return maxnum