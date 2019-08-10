#!/usr/bin/python3
"""8-model_state_fetch_first module
Prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).first()

    if data:
        print("{}: {}".format(data.id, data.name))
    else:
        print("Nothing")
    session.close()
