#!/usr/bin/python3

import json
import os
from  models.base_model import BaseModel

class FileStorage:
    """ This class will help us to serialize and deserialize our dictionaries"""
    __file_path = "file.json"
    __objects = {}

    CLASSES = { "BaseModel" : BaseModel()}

    def all(self):
        """This module returs the __objects dict"""
        return self.__objects
    def new(self, obj):
        """This module set the new dictionary"""
        key = f"{self.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    def save(self):
        """This module serialize the __objecs dict to json file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)
    def reload(self):
        """This module defines the load module"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                
                try:
                    deserialized_objects = json.load(file)
                    for key, values in self.deserialized_objects.items():
                        class_name, obj_id = key.split('.')
                        cls_name = eval(class_name)
                        instance = cls_name(**values)
                        self.__objects[key] = instance
                except Exception as e:
                    pass

