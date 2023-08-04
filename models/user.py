#!/usr/bin/python3
"""clase User"""

import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """clase User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
