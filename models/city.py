#!/usr/bin/python3
"""
Defines city
"""
from models.base_model import BaseModel


class City(BaseModel):

    """Defines City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the city"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns the string representation of the city"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)