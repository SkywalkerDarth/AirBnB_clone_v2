#!/usr/bin/python3
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from os import environ


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """create the engine and drop tables if HBNB_ENV=test"""
        user = environ.get("HBNB_MYSQL_USER")
        password =environ.get("HBNB_MYSQL_PWD")
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