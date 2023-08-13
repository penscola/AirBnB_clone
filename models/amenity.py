#!/usr/bin/python3
"""
Defines amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the amenity"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns the string representation of the amenity"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
