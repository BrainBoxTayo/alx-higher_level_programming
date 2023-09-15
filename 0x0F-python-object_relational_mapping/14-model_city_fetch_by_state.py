#!/usr/bin/python3
'''
    that prints all City objects from the database hbtn_0e_14_usa
'''
import sys
from model_state import State, Base
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dataname = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, dataname))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State, City).outerjoin(
        City).filter(State.id == City.state_id).order_by(City.id)
    for rows in instance:
        print("{}: ({}) {}".format(rows.State.name, rows.City.id,
                                   rows.City.name))
