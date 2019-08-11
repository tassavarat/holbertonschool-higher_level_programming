#!/usr/bin/python3
"""14-model_city_fetch_by_state
Prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine, asc, ForeignKey
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from model_city import City

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for data in session.query(City).join(State).order_by(asc(City.id)).all():
        print("{}: ({}) {}".format(data.state.name, data.id, data.name))
    session.commit()
    session.close()
