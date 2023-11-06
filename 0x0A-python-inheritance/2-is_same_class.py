#!/usr/bin/python3

def is_same_class(obj, a_class):
    """checks if an onbect is exactly an instance of a specified class

    Args:
        obj (any): Object to be checked
        a_class (type) : The Class to be matched the type of obj to

    Returns:
        If Obj is exactly an instance of a_class - True
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
