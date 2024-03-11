#!/usr/bin/python3
"""
Defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review

    Attributes:
        place_id (str): Defines Place id
        user_id (str): Defines User id
        text (str): Review text

    """
    place_id = ""
    user_id = ""
    text = ""
