#!/usr/bin/python3

"""Defines a function that writes into a file"""


def write_file(filename="", text=""):
    """ writing into a file """
    with open(filename, 'w', encoding="utf-8") as fd:
        return fd.write(text)
