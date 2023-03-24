#!/usr/bin/python3
from sqlalchemy import create_engine
from ..base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from ..city import City
from ..place import Place
from ..user import User
from ..review import Review
from ..state import State

classes = {'User': "User",
           'State': "State",
           'Place': "Place",
           'Review': "Review",
           'Amenity': "Amenity"
           }


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """create the engine and drop tables if HBNB_ENV=test"""
        user = environ.get("HBNB_MYSQL_USER")
        password = environ.get("HBNB_MYSQL_PWD")
        host = environ.get("HBNB_MYSQL_HOST", "localhost")
        db = environ.get("HBNB_MYSQL_DB")

        # create the engine
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True
        )

        # drop tables if HBNB_ENV=test
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        if cls:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
        else:
            for i in classes.values():
                obj_query = self.__session.query(i).all()
                for obj in obj_query:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()



