#!/usr/bin/python3
"""
Defines review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the review"""
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """Returns the string representation of the review"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
