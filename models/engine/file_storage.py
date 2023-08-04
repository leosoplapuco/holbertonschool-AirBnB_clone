#!/usr/bin/python3
"""clase FileStorage"""

from json import dump, load, dumps
from os.path import exists
from models import base_model, user, place, state, city, amenity, review

BaseModel = base_model.BaseModel
User = user.User
Place = place.Place
State = state.State
City = city.City
Amenity = amenity.Amenity
Review = review.Review
name_class = ["BaseModel", "City", "State",
              "Place", "Amenity", "Review", "User"]


class FileStorage:
    """FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all"""
        return FileStorage.__objects

    def new(self, obj):
        """new"""
        class_name = obj.__class__.__name__
        id = obj.id
        clas_id = class_name + "." + id
        FileStorage.__objects[clas_id] = obj

    def save(self):
        """save"""
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fil:
            dump(dict_to_json, fil)

    def reload(self):
        """reload"""
        dic_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                dic_obj = load(fil)
                for key, value in dic_obj.items():
                    class_nam = key.split(".")[0]
                    if class_nam in name_class:
                        FileStorage.__objects[key] = eval(class_nam)(**value)
                    else:
                        pass
