#!/usr/bin/python3
""" Defines a Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representing a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing a new Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ prints a string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                    self.x, self.y,
                                                    self.width)
