#!/usr/bin/python3
"""clase Review"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Review(BaseModel):
    """clase Review"""
    place_id = ""
    user_id = ""
    text = ""
