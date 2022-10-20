#!/usr/bin/python3
"""Start link class to table in database."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        result = session.query(State.id).where(State.name == sys.argv[4])
        if result.count() == 0:
            print("Not found")
        else:
            print(result.one().id)
