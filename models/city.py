#!/usr/bin/python3
"""clase City"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""
