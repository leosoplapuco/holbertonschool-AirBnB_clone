#!/usr/bin/python3
"""clase Amenity"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """clase Amenity"""
    name = ""
