#!/usr/bin/python3
""" Addition Module"""


def add_integer(a, b=98):
    """ Function that add two integers/values
    >>> add(2)
    100
    >>> add(2, 5)
    7
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return(int(a + b))
