#!/usr/bin/python3

""" Defines a Rectangle Class that inherits from BaseGeometry  """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents Rectangle Class"""

    def __init__(self, width, height):
        """Initializes a new Rectangle

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area():
        """ find the area of a rectangle """
        return (self.__width * self.__height)

    def __str__():
        return (f'[{self.__class__.__name__}] {self.__width}/{self.height}')
