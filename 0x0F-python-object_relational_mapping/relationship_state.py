#!/usr/bin/python3
''' contains the class definition of a State and
    an instance Base = declarative_base()
    ORM Magic!!
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    ''' Represents a state class for MYSQL database

        __tablename__ (str): The name of the MySQL table to store States
        id (sqlalchemy.Integer): The state's id
        name (sqlalchemy.String): The state's name
        cities (sqlalchemy.orm.relationship): The State-City relationship.

    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
