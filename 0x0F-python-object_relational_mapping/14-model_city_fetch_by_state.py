#!/usr/bin/python3
'''  a script that lists all State objects from the database hbtn_0e_6_usa '''

from sys import argv
import sqlalchemy
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(asc(City.id)):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
