#!/user/bin/python3
"""módulo Base"""

import uuid
from datetime import datetime
from uuid import uuid4
import models
import json

format_dt = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """clase BaseModel"""
    def __init__(self, *args, **kwargs):
        """datos base"""
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_dt)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
