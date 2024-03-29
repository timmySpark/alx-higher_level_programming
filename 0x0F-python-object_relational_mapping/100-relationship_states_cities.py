#!/usr/bin/python3
'''  a script that lists all State objects from the database hbtn_0e_6_usa '''

from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    statement = State(name="California", cities=[City(name="San Francisco")])
    session.add(statement)
    session.commit()
    session.close()
