#!/usr/bin/python3

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for me in my_list:
        avg += (me[0] * me[1])
        size += me[1]
    return (avg / size)
