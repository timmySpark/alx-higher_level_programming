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

    def __str__(self):
        """ Return String Repreentation of a square"""
        return (f"[{self.__class__.__name__}] {self.__size}/{self.__size}")
