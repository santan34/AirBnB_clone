#!/usr/bin/python3
"""
Creates a base class for future use
"""
import uuid
import datetime
import models 

class BaseModel:
    """
    The base class of the project
    """

    def __init__(self, *args, **kwargs):
        """
        initializes the instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def save(self):
        """
        updates the existing objects
        :return: Nothing
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def __str__(self):
        """
        :return: an __str__ of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        The basis of the serialisation
        :return: the object we created
        """
        my_obj = self.__dict__.copy()
        my_obj.update({"__class__": self.__class__.__name__})
        my_obj["created_at"] = self.created_at.isoformat()
        my_obj["updated_at"] = self.updated_at.isoformat()
        return my_obj
