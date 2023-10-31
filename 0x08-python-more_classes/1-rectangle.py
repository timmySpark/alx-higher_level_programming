#!/usr/bin/python3

"""
    class Rectangle that defines a rectangle
"""


class Rectangle:
    """
        Rep a Rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle
            Args:
                width (int)  :- width of a rectangle
                height (int) :- height of the rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ Get/Set width of rectangle """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ Get/Set height of a rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value