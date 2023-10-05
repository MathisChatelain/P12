from sqlalchemy import Column, DateTime, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from utils import use_session

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine("sqlite:///database.db", echo=True)

# Create a base class for declarative models
Base = declarative_base()


# Define the Client model
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, Sequence("client_id_seq"), primary_key=True)
    email = Column(String(100), unique=True)
    phone_number = Column(String(20))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    name = Column(String(50), default="")
    society_name = Column(String(50), default="")
    epic_event_contact = Column(String(50), default="")

    def _to_repr(self):
        return str(f"{self.name}, from {self.society_name}")


# Create the database tables
Base.metadata.create_all(engine)


@use_session
def create_new_client(
    session, email, phone_number, name, society_name, epic_event_contact
):
    created_at = datetime.now()
    updated_at = datetime.now()
    new_client = Client(
        email="",
        phone_number="",
        name="",
        society_name="",
        epic_event_contact="",
        created_at=created_at,
        updated_at=updated_at,
    )
    session.add(new_client)
    return new_client
