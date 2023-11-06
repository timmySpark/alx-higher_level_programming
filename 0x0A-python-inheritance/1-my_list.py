#!/usr/bin/python3
""" Create a List Class """


class MyList(list):
    """ using built-in sort to sort a list"""

    def print_sorted(self):

        """ prints a list in ascending order"""
        print(sorted(self))
