#!/usr/bin/python3

""" Module that defines a rectangle."""


class Rectangle:
    """Class defining rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialises rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Sets and gets width"""
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
        """Sets and gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates and returns area of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a printable rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + "\n"

        return result.rstrip("\n")

    def __repr__(self):
        """ Returns a string representation of the rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ Delete an instance of a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the bigger rectangle based on their areas"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
