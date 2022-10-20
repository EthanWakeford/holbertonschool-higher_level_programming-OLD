#!/usr/bin/python3
"""Start link class to table in database."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy import update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        result = session.query(State).where(State.id == 2).one()
        result.name = "New Mexico"
        session.commit()
