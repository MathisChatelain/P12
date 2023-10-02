from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from utils import use_session

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine("sqlite:///database.db", echo=True)

# Create a base class for declarative models
Base = declarative_base()


# Define the Event model
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, Sequence("event_id_seq"), primary_key=True)


# Create the database tables
Base.metadata.create_all(engine)


@use_session
def create_new_event(session):
    """TODO
    """
    new_event = Event()
    session.add(new_event)
    return new_event