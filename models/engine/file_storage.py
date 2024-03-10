#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User

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
        """
        deserializes the JSON file and loads our object
        """
        current_classes = {'BaseModel': BaseModel, 'User': User}
        if not os.path.exists(FileStorage.__filepath):
            return
        with open(FileStorage.__filepath, 'r') as f:
            obj = None
            try:
                obj = json.load(f)
            except json.JSONDecodeError:
                pass
            if obj is None:
                return
            FileStorage.__objects = {
                    k: current_classes[k.split('.')[0]](**v)
                    for k, v in obj.items()
                    }
