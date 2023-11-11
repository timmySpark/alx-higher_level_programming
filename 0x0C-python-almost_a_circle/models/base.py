#!/usr/bin/python3

""" Representing a base model"""


class Base:
    """ Representing Base Model """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize a Base Class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
