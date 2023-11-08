#!/usr/bin/python3

""" Defines a Class Student"""


class Student:
    """ Represents a Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student
         Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = self.age

    def to_json(self):
        """ retrieves dictionary representation of a student"""
        return self.__dict__