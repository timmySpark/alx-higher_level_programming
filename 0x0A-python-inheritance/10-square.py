#!/usr/bin/python3
""" Defines a Rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represents a Square class """

    def __init__(self, size):
        """ initializes a new Square
        Args:
            size (int): The size of the new Rectangle
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
