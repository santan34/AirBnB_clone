#!/usr/bin/python3
"""
The review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class for the place
    """
    text = ""
    user_id = ""
    place_id = ""
