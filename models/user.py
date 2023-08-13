#!/usr/bin/python3
"""
User creation class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the user"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns the string representation of the user"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
