#!/usr/bin/env python3
import uuid
from datetime import datetime

"""Define a class BaseModel

Public instance attributes:
    id: string - assign with a uuid when an instance is created
        you can use uuid.uuid4() to generate a unique id, but don’t forget to convert to a string
        the goal is to have a unique id for each BaseModel
    created_at: datetime - assign with the current datetime when an instance is created
    updated_at: datetime - assign with the current datetime when an instance is created and updated every time you change your object

Public instance methods:
    save(self): updates the public instance attribute updated_at with the current datetime
    to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance
        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with the class name of the object
        created_at and updated_at must be converted to a string object in ISO format:
            format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            you can use isoformat() of the datetime object
    __str__(self): should print: [<class name>] (<self.id>) <self.__dict__>

This class will be the base for other classes, providing common attributes and methods.
"""
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        cls_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = cls_name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
