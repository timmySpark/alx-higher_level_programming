#!/usr/bin/python3
""" A function that checks for inheritances"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of a class that inherited directly or
    indirectly from the specified class

    Args:
        obj (any): Object to be checked
        a_class (type) : Class to match the type of obj to
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
