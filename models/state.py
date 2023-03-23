#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(BaseModel,Base):
    """ State class """
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
    else:
        name = ''

        @property
        def cities(self):
            '''returns the list of City instances with state_id equals the current State.id
            Filestorage relationship between state and city
            '''
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
