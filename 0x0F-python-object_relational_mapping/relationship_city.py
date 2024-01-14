#!/usr/bin/python3
''' contains the class definition of a City and
    an instance Base = declarative_base()
'''

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    ''' Represents a state city for MYSQL database

        __tablename__ (str): The name of the MySQL table to store cities
        id (sqlalchemy.Integer): The state's id
        name (sqlalchemy.String): The state's name
        state_id: a foreign key to the states table
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
