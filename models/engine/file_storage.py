#!/usr/bin/env python 3
import json
import os
from models.base_model import BaseModel

"""
creates a file stroage class engine
"""


class FileStorage:
    """
    A class that will serve as the storage engine for our project
    """
    __filepath = "file.json"
    __objects:dict = {}

    def all(self):
        """
        Returns all the objetcs
        :return: self__.objects
        """
        return self.__objects

    def new(self, obj):
        """
        adds a new object to our objects
        :param obj: the object to add to __objects
        :return:
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Save  our __objects to a json
        :return: nothing
        """
        ser_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__filepath, "w") as f:
            json.dump(ser_dict, f)

    def reload(self):
        if not os.path.exists(self.__filepath):
            return
        with open(self.__filepath, "r") as file:
            classmap = {"BaseModel": BaseModel}
            obj = None
            try:
                obj = json.load(file)
            except json.JSONDecodeError:
                pass
            if obj is None:
                pass
            else:
                for key, val in obj.items():
                    classname, obj_id = key.split(".")
                    if classname in classmap:
                        obj_class = classmap[classname]
                        object = obj_class(**val)
                        self.__objects[key] = object
