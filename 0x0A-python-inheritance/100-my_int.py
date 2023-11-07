#!/usr/bin/python3

""" Defining Class MyInt """


class MyInt(int):
    """ Representing MyInt Class """

    def __eq__(self, value):
        """ overriding equity (==) operator"""
        return self.real != value

    def __ne__(self, value):
        """Override negation (!=) operator with equity (==) behavior."""
        return self.real == value
