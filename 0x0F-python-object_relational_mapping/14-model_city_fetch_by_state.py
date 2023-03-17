#!/usr/bin/python3
"""
 a script that lists all State objects that contain\
         the letter a from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import city

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(City, State).filter(City.state_id == State.id)\
            .order_by(City.id).all()
    
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()

    session.close()
