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
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of a student"""
        if isinstance(attrs, list):
            result = {value: getattr(self, value) for value in attrs
                      if hasattr(self, value)}
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
