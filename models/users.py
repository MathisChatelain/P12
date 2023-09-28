from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from utils import use_session

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine("sqlite:///database.db", echo=True)

# Create a base class for declarative models
Base = declarative_base()


# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    phone_number = Column(String(20))
    password = Column(String(50))


# Create the database tables
Base.metadata.create_all(engine)


@use_session
def create_new_user(session, name, email, phone_number, password):
    """
    Create a new user ('name', 'email', 'phone_number', 'password')
    in the database and return it, if the user already exist return None
    """
    new_user = User(
        name=name, email=email, phone_number=phone_number, password=password
    )
    session.add(new_user)
    return new_user
