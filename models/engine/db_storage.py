#!/usr/bin/python3
"""Create a mysql engine"""

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """Class to create a engine for a mysql"""

    __engine = None
    __session = None

    def __init__(self):
        """Instatiate for engine"""

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All objects of the session based in the name of the class"""
        obj_dict = {}
        if cls is None:
            all_inst = ["State", "City", "User", "Place", "Review"]

            for cl in all_inst:
                objs = self.__session.query(eval(cl))
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """New object to the database"""
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Save all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object of the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
