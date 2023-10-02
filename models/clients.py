from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from utils import use_session

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine("sqlite:///database.db", echo=True)

# Create a base class for declarative models
Base = declarative_base()


# Define the Client model
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, Sequence("client_id_seq"), primary_key=True)


# Create the database tables
Base.metadata.create_all(engine)


@use_session
def create_new_client(session):
    """TODO
    """
    new_client = Client()
    session.add(new_client)
    return new_client