#!/usr/bin/python3
"""This module defines a class User"""
from base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from place import Place
from review import Review


Base = declarative_base()

class User(BaseModel, Base):
    """This class defines a user by various attributes
    Attributes:
        email: email address
        password: password for login
        first_name: first name
        last_name: last_name
    """
    _tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user',
                        cascade='all, delete, delete-orphan')
    reviews = relationship('Review', backref='user',
                        cascade='all, delete, delete-orphan')
