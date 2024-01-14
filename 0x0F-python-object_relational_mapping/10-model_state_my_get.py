#!/usr/bin/python3
'''  a script that lists all State objects from the database hbtn_0e_6_usa '''

from sys import argv
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    search = argv[4]

    state = session.query(State).filter(
            State.name.like(search)).order_by(asc(State.id)).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
