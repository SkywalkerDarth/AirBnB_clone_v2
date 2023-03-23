#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import decalarative_base

Base = decalarative_base()

class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Attributes:
        state_id: the state id
        name: input name
    """
    __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        places = relationship('Place', backref='cities',
                            cascade='all, delete, delete-orphan')
