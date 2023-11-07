#!/usr/bin/python3

""" Defines a BaseGeometry Class  """


class BaseGeometry():
    """ Represents BaseGEomtry Class"""

    def area(self):
        """ raises an exception with area not implemented message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) !=  int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
