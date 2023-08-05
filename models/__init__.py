#!/usr/bin/python3
"""FileStorage"""

import storage
from models import base_model, user, place, state, city, amenity, review
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State

storage = FileStorage()
storage.reload()
