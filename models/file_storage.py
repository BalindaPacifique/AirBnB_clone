#!/usr/bin/python3

import json
from base_model import BaseModel
from __init__ import storage

class FileStorage:
    """ This class will help us to serialize and deserialize our dictionaries"""
    __file_path = "file.json"
    __objects = {}

    CLASSES = { "BaseModel" : BaseModel}

    def all(self):
        """This module returs the __objects dict"""
        return self.__objects
    def new(self, obj):
        """This module set the new dictionary"""
        key = f"{self.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    def save(self):
        """This module serialize the __objecs dict to json file"""

        for key, obj in self.__objects.items():
            with open(self.__file_path, "w") as file:
                json.dump(self.__objects, file)
    def reload(self):
        """This module defines the load module"""
        with open(self.__file_path, "r") as file:
            seflf.__object = json.load(file)
