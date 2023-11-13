#!/usr/bin/python3
import json

""" Representing a base model"""


class Base:
    """ Representing Base Model """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize a Base Class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                new_list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(new_list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string representation json_string """
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes all already set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = f'{cls.__name__}.json'

        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
