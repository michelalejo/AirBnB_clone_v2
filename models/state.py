#!/usr/bin/python3
"""This is the state class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        cityes = []
        for _id, city in models.storage.all(City).items():
            if self.id == city.state_id:
                cityes.append(city)
        return cityes
