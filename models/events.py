from datetime import datetime

from sqlalchemy import DATE, Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from utils import use_session

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine("sqlite:///database.db", echo=True)

# Create a base class for declarative models
Base = declarative_base()


# Define the Event model
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, Sequence("event_id_seq"), primary_key=True)
    title = Column(String(100))
    contract_id = Column(Integer)
    contact = Column(String(50))
    start_date = Column(DATE, nullable=False, default=datetime.date(datetime.now()))
    end_date = Column(DATE, nullable=False, default=datetime.date(datetime.now()))
    support_contact = Column(String(50))
    location = Column(String(100))
    attendees = Column(Integer, default=0)
    notes = Column(String(100))

    def _to_repr(self):
        return str(f"Event: {self.id}")

    def data_to_str(self):
        return [
            f"{key}: {value}"
            for key, value in self.__dict__.items()
            if isinstance(value, bool) is False
        ]


# Create the database tables
Base.metadata.create_all(engine)


@use_session
def create_new_event(session):
    """TODO"""
    new_event = Event()
    session.add(new_event)
    return new_event


@use_session
def update_event(session, event, **kwargs):
    """
    Update a event with the new values in kwargs
    """
    for key, value in kwargs.items():
        setattr(event, key, value)
    return event


@use_session
def get_event_from_key(session: Session = Session(), key=""):
    """This is a generic function to get a event from a key, since there is no other unique field than the id, for now it is unused"""
    event = session.query(Event).filter(Event.id == key).first()
    for field in []:  # TODO add fields here if needed
        if event:
            return event
        event = session.query(Event).filter(getattr(Event, field) == key).first()
    return None
