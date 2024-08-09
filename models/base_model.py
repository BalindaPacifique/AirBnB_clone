#!/usr/bin/python3

import uuid
from datetime import datetime
import __init__

class BaseModel:
    """ This class will define all public instances attributes and models"""

    def __init__(self, *args,**kwargs):
        """this module defines these public instances attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value =  datetime.fromisoformat(kwargs["created_at"])
                if key == "updated_at":
                    value = datetime.fromisoformat(kwargs["updated_at"])
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ this module defines to doc of the class BaseModel"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This module save and updates the process"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Defines a dictionary which save all the public instances"""

        new_dict = self.__dict__.copy()
        new_dict["class"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
