#!/usr/bin/python3
"""módulo para Base"""

from uuid import uuid4
from datetime import datetime
import json
import models 

format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """clase Basemodel"""
    def __init__(self, *args, **kwargs):
        """ Initialization of Database """
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

    def to_dict(self):
        """to_dict"""
        
        dic = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dic[key] = item

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic


    def __str__(self):
        """str"""
        return("[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__))

    def save(self):
        """save"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
