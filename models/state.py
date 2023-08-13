#!/usr/bin/python3
"""
Class that defines a state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that defines a state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the state"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns the string representation of the state"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
    