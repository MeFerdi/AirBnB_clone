#!/usr/bin/python3
"""
Defines the User Class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User

    Attributes:
        email (str): email of user
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    