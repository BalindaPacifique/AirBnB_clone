from models.base_model import BaseModel
import json

class FileStorage:
    """
    this class will help us to conver our dic string to json one,
    and store it to a json file which will help use to load it again
    """
    __file_path = "file.json"
    __objects = {}
    CLASSES = {
            "BaseModel" : BaseModel()
            }

    def all(self):
        """this module will returns the __objects dictory"""
        return self.__objects
    def new(self, obj):
        """this module will help us to save the dict from basemodel to __objects"""
        key = f"{self.__class__.__name__}.{obj.id}"
        self.__object[key] = self.obj
