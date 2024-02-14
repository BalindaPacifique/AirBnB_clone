#!/usr/bin/env python

import json
from os.path import isfile


class FileStorage:
    """A class for storing and retrieving objects using JSON serialization.

    Private class attributes:
        __file_path (str): The path to the JSON file for storage (default: "file.json").
        __objects (dict): A dictionary to store objects by <class name>.id.

    Public instance methods:
        all(self):
            Returns:
                dict: The dictionary __objects containing all stored objects.

        new(self, obj):
            Sets in __objects the obj with key <obj class name>.id.

        save(self):
            Serializes __objects to the JSON file (path: __file_path).

        reload(self):
            Deserializes the JSON file to __objects (only if the JSON file exists).
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file exists)."""
        if isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    self.__objects[key] = obj_instance
