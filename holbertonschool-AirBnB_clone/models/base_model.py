#!/usr/bin/python3
import models
import uuid
from datetime import datetime

class BaseModel:
    # create public instance attribute
    # public instance attributes are created using the init method
    # they allow other methods to access them and change them
    def __init__(self, *args, **kwargs):
        # a unique id should be printed every time we create a new basemodel
        format_string = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now().isoformat()
        self.created_at = datetime.now().isoformat()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(value,
                                                               format_string)
                    else:
                        self.__dict__[key] = value
        else:
            models.storage.save()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):

        self.__dict__["__class__"] = __class__.__name__
        self.__dict__["updated_at"] = self.updated_at
        self.__dict__["created_at"] = self.created_at
        return (self.__dict__)
    # maintenant we need to send the dictionary of attributes to a json file
    # that will store the attribute values
    # then we need to unload the strings stored inside the json file to object (dict)
    # Reload will be used to transform the list of attributes inside __dict__ that are string into dict object again.
    # key words:
        # deserialize the json file to objects
        # serializes 
        # update models/base_models.py.....
    # execize 6 cherche in google how to build a console
    # and watch the document list  
