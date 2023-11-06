#!/usr/bin/python3
""" Defines a class ad Inherited Class"""


def is_kind_of_class(obj, a_class):
    """ checks if object is an instance of or
    is an instance of a class inherited from the specified class

    Args:
        obj (type) :- object to be checked
        a_class (type) :- the class to be matched with obj

    Returns:
    if Object is an instance of or instance of a class - True
    Otherwise - False

    """

    if isinstance(obj, a_class):
        return True
    return False
