#!/usr/bin/python3
import json


class FileStorage:

    """a class that serializes instances to a JSON
    file and deserializes JSON file to instances"""
    # private class attributes
    __file_path = "file.json"
    # Dictionary to store all objects by <class name>.id
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        # sets in __objects the obj with key <obj class name>.id
        # here the object passed is assumed to have a unique id attribute
        class_name_id: "{}.{}".format(obj.__class__.__name__, obj.id)
        # the key can also be written using the below format
        # class_name_id = f"{obj.__class__.__name__}.{obj.id}"
        __objects[class_name_id] = obj

    def save(self):
        """
        Serializes the instances in __objects
        to a JSON file specified by __file_path.
        """
        with open(FileStorage.__file_path, "w") as f:
            # Create an empty dictionary to store the objects
            data = {}

            # Iterate over the items in
            # __objects and add them to the dictionary
            for key, value in FileStorage.__objects.items():
                # Convert the object to a
                # dictionary and add it to the data dictionary
                data[key] = value.to_dict()

            # Write the data dictionary
            # to the JSON file specified by __file_path
            json.dump(data, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
            for k, v in data.items():
                FileStorage.__objects[k] = eval(v["__class__"])(**v)
        except FileNotFoundError:
            pass
