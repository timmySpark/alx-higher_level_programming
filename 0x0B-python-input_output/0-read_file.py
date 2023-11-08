#!/usr/bin/python3

""" Defines a file that reads text """


def read_file(filename=""):
    """ print the contents of a utf8 text file"""
    with open(filename, encoding="utf-8") as fd:
        print(fd.read(), end="")
