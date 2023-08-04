#!/usr/bin/python3
"""class City"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    """clase City"""
    state_id = ""
    name = ""
