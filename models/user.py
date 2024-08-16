#!/usr/bin/python3
from base_model import BaseModel

class User(BaseModel):
    """This is a class for the user"""

    def __init__(self):
        super.___init__()
        self.email = str("")
        self.password = str("")
        self.first_name = str("")
        self.last_name = str("")
