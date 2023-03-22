#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='add, delete, delete-orphan')

    else:
        name = ''
        state_id = ""
