#!/usr/bin/python3
""" Defines a Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representing a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing a new Square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns arguments to each attributes"""
        attributes = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        if kwargs:
            for (key, value) in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ prints a string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
