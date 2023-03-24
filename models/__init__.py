#!/usr/bin/python3
"""This module instantiates an instance of the Storage will be used"""

from engine.file_storage import FileStorage
from engine.db_storage import DBStorage
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.Review import Review
from models.place import Place
from models.base_model import BaseModel

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
